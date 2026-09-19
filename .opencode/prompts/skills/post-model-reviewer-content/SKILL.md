---
name: post-model-reviewer-content
description: Valida post_content populado por BuildJsonModelPostContent.resolveJsonContent
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: testing
---

## Validação de post_content

Usado pelo agente `post-model-reviewer` para verificar se o mapa
`post_content` gerado por `resolveJsonContent` está populado corretamente
a partir de `post_config`.

### Campos a validar

| Campo | Regra |
|---|---|
| `published` | Copiado de `post_config.published` |
| `scheduled_publish_time` | Copiado de `post_config.scheduled_publish_time` |
| `title` | Copiado de `text_values.title` (se existir) |
| `message` | `text_values.body` (FB feed text / FB feed photo caption via textField) |
| `image_path` | Copiado de `post_config.image_path` |
| `video_path` | Copiado de `post_config.video_path` |
| Campos de texto | Usar `PostType.textField` para determinar chave (`message`, `caption`, `description`) |

### Comportamento tolerante

`resolveJsonContent` **não valida** campos ausentes — preenche o que existe.
Se `post_config` não tem `text_values`, o campo de texto não aparece em
`post_content`. Isso é esperado para `mediaOnly`.

### Exemplo de post_content válido (textWithMedia)

```json
{
  "published": true,
  "title": "Meu post",
  "message": "Conteúdo do post...",
  "image_path": "C:/.../assets/fb_feed_image.jpg"
}
```
