---
name: post-model-reviewer-config
description: Valida post_config gerado por BuildJsonModelPostConfig
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: testing
---

## Validação de post_config

Usado pelo agente `post-model-reviewer` para verificar se o `post_config`
gerado por `BuildJsonModelPostConfig.scanAssets` + `resolveAssetsContent`
está correto para cada bloco da matriz de teste.

### Campos a validar

| Campo | Regra |
|---|---|
| `platform` | Deve ser "facebook" ou "instagram", igual ao bloco |
| `content_type` | Deve ser "feed", "reels" ou "stories", igual ao bloco |
| `media_type` | `textOnly` → "text", `textWithMedia`/`mediaOnly` → "photo" ou "video" conforme extensão |
| `published` | true (agora ou ≤10min) ou false (futuro) conforme timestamp do arquivo |
| `scheduled_publish_time` | null se published=true, ISO8601 se false |
| `retry_config` | `{max_retries: 3, delay_seconds: 2}` |
| `text_values` | Presente se textOnly ou textWithMedia, ausente/null se mediaOnly |
| `text_values.title` | Preenchido a partir do frontmatter title |
| `image_path` | Preenchido se media_type=photo, null caso contrário |
| `video_path` | Preenchido se media_type=video, null caso contrário |
| `image_path`/`video_path` | Nunca ambos preenchidos |

### Exemplo de post_config válido

```json
{
  "platform": "facebook",
  "content_type": "feed",
  "media_type": "photo",
  "published": true,
  "scheduled_publish_time": null,
  "retry_config": {"max_retries": 3, "delay_seconds": 2},
  "text_values": {"title": "Meu post", "body": "Conteúdo..."},
  "image_path": "C:/.../assets/fb_feed_image.jpg",
  "video_path": null
}
```
