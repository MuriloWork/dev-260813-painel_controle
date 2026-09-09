---
name: model-management
description: Regras de criação, manutenção e limpeza de modelos JSON de teste (post_model_NN.json)
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: testing
---

## Estrutura obrigatória

O JSON model deve conter apenas:
```json
{
  "posts": [
    {
      "post_config": { ... },
      "post_content": {}
    }
  ]
}
```

Proibido: return_content, test_timestamp, notes antes do teste.
`post_content` inicia vazio — é populado em runtime por `BuildJsonModelPostContent.resolveJsonContent`.

## post_config

| Campo | Obrigatoriedade | Descrição |
|---|---|---|
| platform | Obrigatório | "facebook" ou "instagram" |
| content_type | Obrigatório | "feed", "reels", "stories" |
| media_type | Obrigatório ou null | "text", "photo", "video" |
| text_path | Obrigatório ou null | Caminho para arquivo de texto |
| text_values | Obrigatório ou null | {title, body} |
| image_path | Obrigatório ou null | Caminho da imagem |
| video_path | Obrigatório ou null | Caminho do vídeo |
| retry_config | Obrigatório | {max_retries, delay_seconds} |
| published | Obrigatório | true (imediato) ou false (agendado) |
| scheduled_publish_time | Obrigatório ou null | ISO8601 se published=false, null se true |

Regras:
- Todos os campos presentes (mesmo que null)
- image_path e video_path nunca ambos com valor
- Prioridade texto: text_path > text_values.body
- published + scheduled_publish_time definem agendamento

## post_content

Construído automaticamente pelo pipeline. Não preencher manualmente.

## Procedimento de teste
1. Criar src/data/post_model_NN.json (NN sequencial)
2. Atualizar json_model.file em src/scripts/config.json
3. Verificar arquivos de mídia existem
4. Validar published + scheduled_publish_time coerentes
5. Executar dart src/scripts/posts_service_post.dart
6. Avaliar log e resposta
