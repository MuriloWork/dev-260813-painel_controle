---
name: post-model-reviewer-result
description: Valida PostContent gerado por resolveContentRouter
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: testing
---

## Validação de PostContent

Usado pelo agente `post-model-reviewer` para verificar se o objeto
`PostContent` final gerado por `resolveContentRouter` + builder
(FbBuilder/IgBuilder) está correto.

### Campos a validar

| Campo | Regra |
|---|---|
| `type` | `TextContent` (media_type=text), `ImageContent` (photo), `VideoContent` (video) |
| `filePath` | Caminho absoluto do arquivo de mídia, ou null para textOnly |
| `build()` | `TextContent` → `{message: ...}`, `ImageContent` → `{file: ..., caption?: ...}`, `VideoContent` → `{file: ..., description?: ...}` |
| `uploadFlow` | FB: simple (feed photo/text), resumable (feed video), threeStep (reels, stories video), twoStep (stories photo). IG: igContainer (feed photo), igResumable (reels, stories) |

### Mapeamento content_type + media_type → PostContent

| content_type | media_type | PostContent | uploadFlow |
|---|---|---|---|
| feed | text | `TextContent(message)` | simple |
| feed | photo | `ImageContent(filePath, caption)` | simple |
| feed | video | `VideoContent(filePath, description)` | resumable |
| reels | video | `VideoContent(filePath, description)` | threeStep |
| stories | photo | `ImageContent(filePath, caption)` | twoStep |
| stories | video | `VideoContent(filePath, description)` | threeStep |

### Exemplo de validação

```dart
// FB feed photo
final result = resolveContentRouter(postType, null, postContent);
assert(result is ImageContent);
assert(result.filePath == postContent['image_path']);
assert(result.build()['caption'] == postContent['caption']);
```
