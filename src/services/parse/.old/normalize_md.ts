import * as fs from 'fs';
import * as path from 'path';

interface Heading {
  level: number;
  originalText: string;
  numberedText: string;
  anchor: string;
  lineNumber: number;
}

interface HeadingNumberingState {
  counters: number[];
  headings: Heading[];
}

/**
 * Formata a numeração hierárquica com ponto final
 * Ex: [1, 2, 3] → "1.2.3."
 */
function formatNumbering(counters: number[]): string {
  return counters.slice(0, counters.length).join('.') + '.';
}

/**
 * Cria anchor no formato GitHub (kebab-case, sem pontos, minúsculo)
 * Ex: "1.1. Título" → "11-titulo"
 */
function createAnchor(text: string): string {
  return text
    .toLowerCase()
    .replace(/\./g, '')           // Remove pontos da numeração
    .replace(/[àáâãäå]/g, 'a')
    .replace(/[èéêë]/g, 'e')
    .replace(/[ìíîï]/g, 'i')
    .replace(/[òóôõö]/g, 'o')
    .replace(/[ùúûü]/g, 'u')
    .replace(/ç/g, 'c')
    .replace(/[^a-z0-9\s-]/g, '') // Remove caracteres especiais
    .trim()
    .replace(/\s+/g, '-');        // Espaços viram hífens
}

/**
 * Verifica se uma linha está dentro de um code block
 */
function isInsideCodeBlock(lineIndex: number, codeBlockLines: Array<[number, number]>): boolean {
  for (const [start, end] of codeBlockLines) {
    if (lineIndex >= start && lineIndex <= end) {
      return true;
    }
  }
  return false;
}

/**
 * Encontra todos os code blocks (``` ou ~~~) no conteúdo
 * Retorna array de tuplas [linha_inicio, linha_fim]
 */
function findCodeBlocks(lines: string[]): Array<[number, number]> {
  const codeBlocks: Array<[number, number]> = [];
  let inBlock = false;
  let blockStart = -1;
  let fenceChar = '';

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    
    if (!inBlock && (line.startsWith('```') || line.startsWith('~~~'))) {
      inBlock = true;
      blockStart = i;
      fenceChar = line[0];
    } else if (inBlock && line.startsWith(fenceChar.repeat(3))) {
      codeBlocks.push([blockStart, i]);
      inBlock = false;
      blockStart = -1;
    }
  }

  return codeBlocks;
}

/**
 * Aplica numeração hierárquica nos headings do markdown
 * Numera apenas a partir do H2 (level >= 2)
 */
function applyHeadingNumbering(content: string): { numberedContent: string; headings: Heading[] } {
  const lines = content.split('\n');
  const codeBlocks = findCodeBlocks(lines);
  const state: HeadingNumberingState = {
    counters: [],
    headings: [],
  };

  const numberedLines = lines.map((line, lineIndex) => {
    // Pula linhas dentro de code blocks
    if (isInsideCodeBlock(lineIndex, codeBlocks)) {
      return line;
    }

    // Regex para detectar headings (# a ######) - inclui \r para Windows
    const headingMatch = line.match(/^(#{1,6})\s+(.+)\r?$/);

    if (!headingMatch) {
      return line;
    }

    const [, hashes, text] = headingMatch;
    const level = hashes.length;

    // Remove numeração existente se houver (ex: "1.1. Título" → "Título")
    const textWithoutNumbering = text.replace(/^\d+(\.\d+)*\.\s*/, '');

    // H1 não é numerado, apenas adicionado ao TOC
    if (level === 1) {
      state.counters = []; // Reseta contadores ao encontrar H1
      state.headings.push({
        level,
        originalText: textWithoutNumbering,
        numberedText: textWithoutNumbering,
        anchor: createAnchor(textWithoutNumbering),
        lineNumber: lineIndex,
      });
      return line; // Mantém H1 sem alteração
    }

    // Atualiza contadores (ajusta índice para H2 ser o primeiro)
    state.counters[level - 2] = (state.counters[level - 2] || 0) + 1;
    state.counters = state.counters.slice(0, level - 1);

    // Formata numeração
    const numbering = formatNumbering(state.counters);
    const numberedText = `${numbering} ${textWithoutNumbering}`;
    const anchor = createAnchor(numberedText);

    state.headings.push({
      level,
      originalText: textWithoutNumbering,
      numberedText,
      anchor,
      lineNumber: lineIndex,
    });

    return `${'#'.repeat(level)} ${numberedText}`;
  });

  return {
    numberedContent: numberedLines.join('\n'),
    headings: state.headings,
  };
}

/**
 * Gera Table of Contents (TOC) a partir dos headings
 */
function generateTOC(headings: Heading[]): string {
  if (headings.length === 0) {
    return '# Table of Contents\n\n*Sem seções encontradas.*\n';
  }

  const tocLines = ['# Table of Contents', ''];

  for (const heading of headings) {
    const indent = '  '.repeat(heading.level - 1);
    const link = `[${heading.numberedText}](#${heading.anchor})`;
    tocLines.push(`${indent}- ${link}`);
  }

  return tocLines.join('\n') + '\n';
}

/**
 * Função principal
 */
function main(): void {
  const filePath = process.argv[2];

  if (!filePath) {
    console.error('Uso: ts-node normalize_md.ts <arquivo.md>');
    console.error('Exemplo: ts-node normalize_md.ts sprints\\spot.md');
    process.exit(1);
  }

  // Valida arquivo
  if (!fs.existsSync(filePath)) {
    console.error(`Erro: Arquivo não encontrado: ${filePath}`);
    process.exit(1);
  }

  const ext = path.extname(filePath).toLowerCase();
  if (ext !== '.md') {
    console.warn(`Aviso: Arquivo não tem extensão .md (${ext})`);
  }

  // Lê conteúdo
  const content = fs.readFileSync(filePath, 'utf-8');
  const originalLineCount = content.split('\n').length;

  // Aplica numeração
  const { numberedContent, headings } = applyHeadingNumbering(content);

  // Salva arquivo editado
  fs.writeFileSync(filePath, numberedContent, 'utf-8');

  // Gera e salva TOC
  const dir = path.dirname(filePath);
  const name = path.basename(filePath, '.md');
  const tocPath = path.join(dir, `${name}_toc.md`);
  
  const toc = generateTOC(headings);
  fs.writeFileSync(tocPath, toc, 'utf-8');

  // Resumo
  console.log(`✓ ${headings.length} seções numeradas`);
  console.log(`✓ TOC criado em: ${tocPath}`);
  console.log(`\nNíveis encontrados:`);
  
  const levelCounts = new Map<number, number>();
  for (const h of headings) {
    levelCounts.set(h.level, (levelCounts.get(h.level) || 0) + 1);
  }
  
  for (const [level, count] of levelCounts.entries()) {
    console.log(`  H${level}: ${count}`);
  }
}

main();
