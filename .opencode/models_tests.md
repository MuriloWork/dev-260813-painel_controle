**Regras de Configuração de Modelos e Execução de Testes**

# 1. Regras para o JSON Model (`post_model_NN.json`)

## 1.1. 1 Estrutura Obrigatória

O JSON model deve conter apenas:

```json
{
  "posts": [
    {
      "source_content": { ... },
      "post_content": { ... }
    }
  ]
}
```

**Proibido:** `return_content`, `test_timestamp`, `notes` antes do teste.
**Remova esses campos** sempre ao preparar um novo cenário.

## 1.2. 2 Campos de `source_content`

| Campo          | Obrigatoriedade | Descrição                                              |
| -------------- | --------------- | ------------------------------------------------------ |
| `image_path`   | Obrigatório     | Caminho da imagem. `null` se não houver                |
| `video_path`   | Obrigatório     | Caminho do vídeo. `null` se não houver                 |
| `text_path`    | Obrigatório     | Caminho para arquivo de texto. `null` se não houver    |
| `text_value`   | Obrigatório     | Texto direto. `null` se não houver                     |
| `retry_config` | Obrigatório     | Configuração de retry (`max_retries`, `delay_seconds`) |

**Regras:**
- **Todos os campos são de presença obrigatória** no modelo — se não for utilizado, deve ter valor `null`
- `image_path` e `video_path` **nunca** podem ter valor simultaneamente
- Usar arquivos em `./src/assets/post_test/` para caminhos de [image_path, video_path, text_path]
- O texto final é resolvido por prioridade: `text_path` > `text_value` > "Default message"

## 1.3. 3 Campos de `post_content`

| Campo                    | Obrigatoriedade | Valores permitidos                                                                     |
| ------------------------ | --------------- | -------------------------------------------------------------------------------------- |
| `platform`               | Obrigatório     | `facebook`                                                                             |
| `content_type`           | Obrigatório     | `feed`, `reels`, `stories`                                                             |
| `media_type`             | Obrigatório     | `text`, `photo`, `video`                                                               |
| `message`                | Obrigatório     | `null` se não usado. Apenas para `media_type: text` + `content_type: feed`             |
| `caption`                | Obrigatório     | `null` se não usado. Apenas para `media_type: photo` + `content_type: feed`/`stories`  |
| `description`            | Obrigatório     | `null` se não usado. Para `media_type: video` em qualquer `content_type`               |
| `published`              | Obrigatório     | `true` (imediato) ou `false` (agendado)                                                |
| `scheduled_publish_time` | Obrigatório     | ISO 8601 se `published: false`, `null` se `published: true`                            |

**Regras:**
- **Todos os campos são de presença obrigatória** — se não utilizado, valor `null`
- **`title` e `content_title`** não existem na API. Nunca usar.
- **`midia_endpoint` removido** — endpoint é definido pelo script com base em `content_type` + `media_type`
- Apenas **um** campo de texto é preenchido automaticamente pelo script:
  - `media_type: text` → preenche `message`
  - `media_type: photo` → preenche `caption`
  - `media_type: video` → preenche `description`

## 1.4. 4 Mapeamento `content_type` + `media_type` → Endpoint

| `content_type` | `media_type` | Endpoint da API                                 |
|----------------|-------------|-------------------------------------------------|
| `feed`         | `text`      | `/{page-id}/feed`                               |
| `feed`         | `photo`     | `/{page-id}/photos`                             |
| `feed`         | `video`     | `/{page-id}/videos`                             |
| `reels`        | `video`     | `/{page-id}/videos` (+ privacidade PUBLIC)      |
| `stories`      | `video`     | `/{page-id}/video_stories` (upload em 3 etapas) |
| `stories`      | `photo`     | `/{page-id}/photos` → `/{page-id}/photo_stories` (2 etapas) |

## 1.5. 5 Regras Específicas por Tipo

**Feed:**
- Usar `published` + `scheduled_publish_time` para agendamento
- Texto vai no campo correspondente (`message`, `caption`, `description`)

**Reels:**
- **Não** usar `title` ou `content_title`
- A privacidade `PUBLIC` é adicionada automaticamente pelo script
- Sempre `media_type: video`

**Stories:**
- Vídeo: fluxo de 3 etapas (`/video_stories` com `upload_phase`)
- Foto: fluxo de 2 etapas (`/photos` com `published=false` → `/photo_stories` com `photo_id`)
- Texto vai em `description` (vídeo) ou `caption` (foto, enviado na etapa 1)
- **⚠️ Stories NÃO suportam agendamento via API pública** — `scheduled_publish_time` e `published=false` são ignorados. `published` deve ser `true`. Confirmado por teste prático e docs oficiais.
- `/photo_stories` só aceita `photo_id` (sem `scheduled_publish_time` ou `published`)
- `/video_stories` finish não deve enviar `video_state` (comportamento padrão = PUBLISHED)
- `video_state=SCHEDULED` listado na doc de `/video_stories` não funciona na prática

# 2. Procedimento de Teste

## 2.1. 1 Preparação

1. **Criar/limpar JSON:** `src/data/post_model_NN.json`
   - Novo cenário: criar `post_model_NN.json` com **todos os campos obrigatórios**
   - Cenário existente: manter campos, remover `return_content`, `test_timestamp`, `notes`
   - Atualizar `source_content` e `post_content`

2. **Atualizar config.json:** `src/scripts/config.json`
   - Alterar `json_model.file` para `post_model_NN.json`

3. **Verificar arquivos de mídia:**
   - Confirmar que `image_path` ou `video_path` existem
   - Caminhos com espaços → usar `C:/...` (barra normal)

4. **Validar JSON manualmente:**
   - Todos os campos obrigatórios presentes (mesmo que `null`)
   - `image_path` e `video_path` não ambos com valor
   - `published` e `scheduled_publish_time` coerentes

## 2.2. 2 Execução

```bash
dart src/scripts/posts_service_post.dart
```

**Sempre** da raiz do projeto, com caminho relativo completo.

## 2.3. 3 Avaliação

1. Verificar log:
   - Endpoint correto para o tipo de conteúdo
   - Campos enviados fazem sentido
   - Status 200

2. Na resposta:
   - `feed`/`reels` → `id`
   - `stories` → `post_id`

3. Atualizar JSON model com `return_content` do script

# 3. Regras de Edição para Agentes

## 3.1. 1 O que NÃO fazer

- ❌ Instruir o usuário a editar arquivos — o agente EDITA diretamente
- ❌ Assumir que documentação da Meta está correta — testar sempre
- ❌ Usar `title` ou `content_title` como campo de envio
- ❌ Misturar `image_path` e `video_path` simultaneamente
- ❌ Deixar campos obsoletos no JSON (sempre limpar antes do teste)
- ❌ Remover campos do JSON model (devem ficar como `null`)

## 3.2. 2 O que o script faz automaticamente

- Preenche o campo de texto correto baseado em `media_type`
- Adiciona `privacy: PUBLIC` para reels
- Salva dados de retorno no JSON model
- Define endpoint baseado em `content_type` + `media_type`

## 3.3. 3 Validações pré-execução

1. JSON model tem `posts[0].source_content` + `post_content`
2. Todos os campos obrigatórios presentes
3. `content_type` e `media_type` são combinação válida
4. Caminhos de mídia existem
5. `published` e `scheduled_publish_time` coerentes
6. Config.json aponta para o modelo correto

# 4. cenarios de teste e suas variantes

