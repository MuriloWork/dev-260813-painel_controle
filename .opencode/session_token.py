import sqlite3
import json
import os
import sys
from datetime import datetime, timezone
from collections import defaultdict

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

DB_PATH = os.path.expanduser(
    r"~\.local\share\opencode\opencode.db"
)
SESSION_ID = None


def connect():
    if not os.path.exists(DB_PATH):
        print(f"[ERRO] Banco não encontrado: {DB_PATH}")
        sys.exit(1)
    return sqlite3.connect(DB_PATH)


def find_active_session(conn):
    if SESSION_ID:
        cur = conn.execute(
            "SELECT id, title, model, tokens_input, tokens_output, "
            "tokens_reasoning, tokens_cache_read, time_created, time_updated "
            "FROM session WHERE id = ?", (SESSION_ID,)
        )
        row = cur.fetchone()
        if not row:
            print(f"[ERRO] Sessão {SESSION_ID} não encontrada")
            sys.exit(1)
        return row

    cur = conn.execute(
        "SELECT id, title, model, tokens_input, tokens_output, "
        "tokens_reasoning, tokens_cache_read, time_created, time_updated "
        "FROM session ORDER BY time_updated DESC LIMIT 1"
    )
    return cur.fetchone()


def ts(epoch_ms):
    return datetime.fromtimestamp(epoch_ms / 1000, tz=timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S"
    )


def fmt(n):
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)


def tok(n):
    return n // 4


def bar(pct, width=30):
    filled = int(pct / 100 * width)
    return "#" * filled + "-" * (width - filled)


def analyze():
    conn = connect()
    session = find_active_session(conn)
    sid, title, model_json, t_in, t_out, t_reason, t_cache, t_cre, t_up = session

    try:
        model_name = json.loads(model_json).get("id", model_json)
    except Exception:
        model_name = str(model_json)

    print("=" * 62)
    print("  SESSION TOKEN ANALYZER")
    print("=" * 62)
    print(f"  Sessão:    {sid}")
    print(f"  Título:    {title}")
    print(f"  Modelo:    {model_name}")
    print(f"  Criado:    {ts(t_cre)}")
    print(f"  Atualizado: {ts(t_up)}")
    print(f"  Tokens acumulados (session table):")
    print(f"    Input:    {fmt(t_in)}")
    print(f"    Output:   {fmt(t_out)}")
    print(f"    Reasoning: {fmt(t_reason)}")
    print(f"    Cache read: {fmt(t_cache)}")

    # -- Scan parts -----------------------------------------------------------
    cur = conn.execute(
        "SELECT time_created, data FROM part "
        "WHERE session_id = ? ORDER BY time_created", (sid,)
    )
    rows = cur.fetchall()

    # Aggregators
    type_counts = defaultdict(int)
    type_bytes = defaultdict(int)
    tool_counts = defaultdict(int)
    tool_bytes = defaultdict(int)
    tool_failed = 0
    file_reads = []  # (filename, bytes)
    text_parts = []
    step_finishes = []

    for epoch_ms, raw in rows:
        try:
            part = json.loads(raw)
        except json.JSONDecodeError:
            continue

        ptype = part.get("type", "unknown")
        data_len = len(raw)
        type_counts[ptype] += 1
        type_bytes[ptype] += data_len

        if ptype == "tool":
            tool_name = part.get("tool", "?")
            state = part.get("state", {})
            status = state.get("status", "")
            tool_counts[tool_name] += 1
            tool_bytes[tool_name] += data_len
            if status == "error":
                tool_failed += 1

            if tool_name == "read":
                inp = state.get("input", {})
                fpath = inp.get("filePath", "")
                fname = os.path.basename(fpath) if fpath else "(unknown)"
                file_reads.append((fname, data_len))

        elif ptype == "text":
            text = part.get("text", "")
            text_parts.append((data_len, text[:120]))

        elif ptype == "step-finish":
            tokens = part.get("tokens", {})
            step_finishes.append(tokens)

    total_parts = len(rows)
    total_bytes = sum(len(r[1]) for r in rows)

    # -- Summary stats --------------------------------------------------------
    tool_total = type_bytes.get("tool", 0)
    text_total = type_bytes.get("text", 0)
    reasoning_total = type_bytes.get("reasoning", 0)
    other_total = total_bytes - tool_total - text_total - reasoning_total

    print()
    print(f"  Partes na sessão: {total_parts}")
    print(f"  Dados brutos totais: {fmt(total_bytes)} bytes")
    print()

    # -- Token flow from step-finish ------------------------------------------
    if step_finishes:
        last_tokens = step_finishes[-1]
        peak = max(t.get("total", 0) for t in step_finishes)
        print("  FLUXO DE TOKENS (último step-finish):")
        last_total = last_tokens.get("total", 0)
        last_in = last_tokens.get("input", 0)
        last_out = last_tokens.get("output", 0)
        last_reas = last_tokens.get("reasoning", 0)
        last_cache = last_tokens.get("cache", {})
        print(f"    Total:         {fmt(last_total)}")
        print(f"    Input:         {fmt(last_in)}")
        print(f"    Output:        {fmt(last_out)}")
        print(f"    Reasoning:     {fmt(last_reas)}")
        print(f"    Cache read:    {fmt(last_cache.get('read', 0))}")
        print(f"    Pico total:    {fmt(peak)}")
        print(f"    Steps:         {len(step_finishes)}")
    else:
        print("  [sem dados de step-finish]")

    # -- Breakdown by type ----------------------------------------------------
    print()
    print("  BREAKDOWN POR TIPO DE PARTE:")
    print(f"    {'Tipo':<20} {'Qtd':>5} {'Bytes':>10} {'Tokens':>8} {'%':>6}")
    print(f"    {'-'*20} {'-'*5} {'-'*10} {'-'*8} {'-'*6}")
    for ptype in ["tool", "text", "reasoning", "step-start", "step-finish"]:
        n = type_counts.get(ptype, 0)
        b = type_bytes.get(ptype, 0)
        pct = b / total_bytes * 100 if total_bytes else 0
        print(f"    {ptype:<20} {n:>5} {fmt(b):>10} {fmt(tok(b)):>8} {pct:>5.1f}% {bar(pct)}")

    other_n = sum(v for k, v in type_counts.items()
                  if k not in ("tool", "text", "reasoning", "step-start", "step-finish"))
    other_b = sum(v for k, v in type_bytes.items()
                  if k not in ("tool", "text", "reasoning", "step-start", "step-finish"))
    if other_n:
        print(f"    {'outros':<20} {other_n:>5} {fmt(other_b):>10} "
              f"{fmt(tok(other_b)):>8} {other_b/total_bytes*100:>5.1f}%")

    # -- Tool breakdown -------------------------------------------------------
    print()
    print("  BREAKDOWN POR FERRAMENTA:")
    print(f"    {'Ferramenta':<18} {'Chamadas':>9} {'Bytes':>10} {'Tokens':>8} {'%':>6}")
    print(f"    {'-'*18} {'-'*9} {'-'*10} {'-'*8} {'-'*6}")
    for tname in sorted(tool_counts, key=lambda t: tool_bytes[t], reverse=True):
        n = tool_counts[tname]
        b = tool_bytes[tname]
        pct = b / tool_total * 100 if tool_total else 0
        print(f"    {tname:<18} {n:>9} {fmt(b):>10} {fmt(tok(b)):>8} {pct:>5.1f}% {bar(pct)}")

    if tool_failed:
        print(f"\n    [ERROS] {tool_failed} chamadas com falha")

    # -- Top file reads -------------------------------------------------------
    if file_reads:
        file_agg = defaultdict(int)
        file_count = defaultdict(int)
        for fname, sz in file_reads:
            file_agg[fname] += sz
            file_count[fname] += 1
        sorted_files = sorted(file_agg.items(), key=lambda x: x[1], reverse=True)

        print()
        print("  TOP ARQUIVOS LIDOS (por bytes):")
        print(f"    {'Arquivo':<40} {'Vezes':>6} {'Bytes':>10} {'Tokens':>8}")
        print(f"    {'-'*40} {'-'*6} {'-'*10} {'-'*8}")
        for fname, sz in sorted_files[:15]:
            n = file_count[fname]
            print(f"    {fname:<40} {n:>6} {fmt(sz):>10} {fmt(tok(sz)):>8}")
        if len(sorted_files) > 15:
            others = sorted_files[15:]
            other_sz = sum(s for _, s in others)
            other_cnt = sum(file_count[f] for f, _ in others)
            print(f"    {'... mais ' + str(len(others)) + ' arquivos':<40} "
                  f"{other_cnt:>6} {fmt(other_sz):>10} {fmt(tok(other_sz)):>8}")

    # -- Text samples ---------------------------------------------------------
    print()
    print("  AMOSTRAS DE TEXTO (mensagens trocadas):")
    for sz, snippet in text_parts:
        snippet_oneline = snippet.replace("\n", " ").strip()
        if len(snippet_oneline) > 100:
            snippet_oneline = snippet_oneline[:100] + "..."
        print(f"    [{fmt(sz):>6}B] {snippet_oneline}")
        if len(text_parts) > 12:
            print(f"    ... e mais {len(text_parts) - 12} partes de texto")
            break

    # -- Summary comparison with tokenscope -----------------------------------
    print()
    print("=" * 62)
    print("  CORRELAÇÃO COM TOKENSCOPE")
    print("=" * 62)
    print(f"  Tokenscope reportou: ~89.948 tokens (input + output)")
    print(f"  Breakdown SQLite (bytes brutos das partes):")
    print(f"    Tool parts:   {fmt(tool_total):>10}B  ~{fmt(tok(tool_total)):>8} tokens")
    print(f"    Text parts:   {fmt(text_total):>10}B  ~{fmt(tok(text_total)):>8} tokens")
    print(f"    Reasoning:    {fmt(reasoning_total):>10}B  ~{fmt(tok(reasoning_total)):>8} tokens")
    print(f"    {'─'*42}")
    print(f"    Total parts:  {fmt(total_bytes):>10}B  ~{fmt(tok(total_bytes)):>8} tokens est.")
    print()
    print(f"  [!] Estimativa: ~4 bytes = 1 token. Valor real varia por tokenizer.")
    print()
    print(f"  Dica: os ~{fmt(tok(tool_total))} tokens de ferramenta dominam o contexto.")
    print(f"  Use /compact ou /new para limpar.")

    conn.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        SESSION_ID = sys.argv[1]
    analyze()
