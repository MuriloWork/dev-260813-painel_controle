---
name: instagram-api
description: Regras e mapeamento da API Instagram para criação de posts no projeto Meta API
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: instagram-posting
---

## Endpoints Instagram

### Container creation
POST /{igUserId}/media

| Parâmetro | Obrigatório | Descrição |
|---|---|---|
| media_type | Sim | IMAGE, VIDEO, CAROUSEL, REELS, STORIES |
| image_url | Condicional | URL pública da imagem (ou file upload) |
| video_url | Condicional | URL pública do vídeo (ou file upload) |
| caption | Não | Texto do post (sempre caption, diferente do FB) |
| location_id | Não | ID de local |
| children | CAROUSEL | IDs de mídia para carrossel |
| collaborators | Não | Usuários colaboradores |
| share_to_feed | REELS | Se aparece também no feed |

### Container publish
POST /{igUserId}/media_publish
- Parâmetro: creation_id (obrigatório)
- scheduled_publish_time: só para feed IMAGE/VIDEO/CAROUSEL

## Mapeamento content_type + media_type → API

| content_type | media_type (model) | IG media_type | Fluxo |
|---|---|---|---|
| feed | photo | IMAGE | container → publish |
| feed | video | VIDEO | container → publish |
| reels | video | REELS | container → publish |
| stories | photo | STORIES | container → publish |
| stories | video | STORIES | container → publish |

## Diferenças Instagram vs Facebook

| Aspecto | Facebook | Instagram |
|---|---|---|
| Token | page_access_token (derivado) | user_token (FB_ACCESS_TOKEN direto) |
| ID alvo | pageId | igUserId (Business Account) |
| Fluxo | 4 variações | Universal: container → publish |
| Agendamento | Feed/Reels via parâmetros específicos | Só feed IMAGE/VIDEO |
| Texto | message/caption/description | Sempre caption |
| Permalink | facebook.com/{id} | instagram.com/p/{media_id} |

## Abordagem PS1-first
Toda interação com API Instagram deve ser validada via PowerShell antes do Dart.
Consultar sprints/meta_api_docs/ antes de qualquer chamada.
