
# regex [regex](file:///C:/Users/muril/OneDrive/01%20mycloud/01%20sistMu/20.01%20obsidianPkm/20%20km_ssg/10_info_km_ssg/20%20%20automacao/02_parsing_regex/251012%20regex.md)

# opencode

para obter modelos gemini da versao v1beta

```powershell
curl.exe -UseBasicParsing "https://generativelanguage.googleapis.com/v1beta/models?key=AIzaSyD5IqlnTeWbW5odjzAQ_QfN2EtkCgrh0Mw" | Select-Object -ExpandProperty Content | Out-File -FilePath models.json -Encoding utf8; type models.json
```
- models/gemini-2.5-flash
- models/gemini-2.5-pro
- models/gemini-2.0-flash
- models/gemini-flash-latest

# python 

## venv [venv](file:///C:/Users/muril/OneDrive/01%20mycloud/01%20sistMu/20.01%20obsidianPkm/20%20km_ssg/10_info_km_ssg/20%20%20automation/10.03%20python/251023%20venv.md)

ativar venv: C:\Users\muril\venvs\pessoal\Scripts\Activate.ps1

# banco de dados

## wsl [help](file:///C:/Users/muril/OneDrive/01%20mycloud/01%20sistMu/20.01%20obsidianPkm/20%20km_ssg/10_info_km_ssg/20%20%20automacao/01_msWindows/WSL%20linux%20bash.md)

- docker volume ls | grep supabase
- docker inspect supabase_db_260402_crm_cdd | grep -A 10 "Mounts"
- listar containers: 
  - docker ps
  - docker ps --format "table {{.Names}}\t{{.Image}}"
  - docker ps --filter "name=supabase_db" --format "{{.Names}}"
- entrar no container: docker exec -it supabase_db_260402_crm_cdd bash
- entrar usando psql: 
  - psql "postgresql://usuario:senha@127.0.0.1:PORTA/banco"
  - psql "postgresql://supabase_admin:postgres@127.0.0.1:54322/postgres"
- Restaurar backup: 
  - psql "postgresql://supabase_admin:postgres@127.0.0.1:54322/postgres" -f "C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\dbMu\supabase_251113_sistMuFin\dump-postgres-202605051735.sql"
- select
  - verifica quantos registros existem nas tabelas principais
    ```bash
    docker exec supabase_db_260402_crm_cdd psql -U postgres -d postgres -c "
    SELECT 'contacts' as tabela, COUNT(*) FROM public.contacts
    UNION ALL
    SELECT 'companies', COUNT(*) FROM public.companies
    UNION ALL
    SELECT 'sync.master_contacts', COUNT(*) FROM sync.master_contacts
    UNION ALL
    SELECT 'sync.google_contacts', COUNT(*) FROM sync.google_contacts;
    "
    ```

## docker

  - listar todos os bancos: psql -U postgres -c "\l"
  - listar todos os bancos: psql -U supabase_admin -c "\l"
  - conectar ao banco: psql -U postgres -d postgres
  - conectar ao banco: psql -U postgres -d supabase_admin
  - Verificar qual usuário existe neste container: docker exec supabase_db_supabase_251113_sistMuFin psql -U supabase_admin -d postgres -c "\du"

## postgresql [bin](file:///C:/Program%20Files/PostgreSQL/18/bin)

- psql
  - sair do psql: \q
  - limpar tela: \! clear
  - listar bancos: \l
  - listar schemas: \dt, \dn
  - listar tabelas: \dt public.*
- encontrar container: docker exec supabase_db_260402_crm_cdd ls -la /var/lib/postgresql/data
- ver os bancos (pastas numeradas em base/): ls -la /var/lib/postgresql/data/base
- acessar supabase local via URL
  - Pelo terminal (psql): psql "postgresql://postgres:postgres@127.0.0.1:54322/postgres"
  - comandos agrupados
    - Vários -c (comandos separados): psql "postgresql://postgres:postgres@127.0.0.1:54322/postgres" -c "\dt public.*" -c "SELECT COUNT(*) FROM public.contacts;"
    - Um -c com vários comandos (ponto e vírgula): psql "postgresql://postgres:postgres@127.0.0.1:54322/postgres" -c "\dt public.*; SELECT COUNT(*) FROM public.contacts;"
    - arquivo com vários comandos (-f):
      ```bash
      # Criar arquivo com comandos
      echo "\dt public.*" > comandos.sql
      echo "SELECT COUNT(*) FROM public.contacts;" >> comandos.sql
      # Executar
      psql "postgresql://postgres:postgres@127.0.0.1:54322/postgres" -f comandos.sql
      ```
    - Comandos no estilo "here document" (bash):
      ```bash
      psql "postgresql://postgres:postgres@127.0.0.1:54322/postgres" <<EOF
      \dt public.*
      SELECT COUNT(*) FROM public.contacts;
      \q
      EOF
      ```
  - Pelo Docker: docker exec -it supabase_db_260402_crm_cdd psql -U postgres -d postgres
  - DBeaver:
    - Host: 127.0.0.1
    - Port: 54322
    - User: postgres
    - Password: postgres
    - Database: postgres
  - Por código (Dart/Flutter, ex.):
    ```dart
      final conn = PostgreSQLConnection(
        '127.0.0.1', 
        54322, 
        'postgres', 
        username: 'postgres', 
        password: 'postgres'
      );
    ```
- backups locais:
  - Backup completo (schema + dados): pg_dump "postgresql://postgres:postgres@127.0.0.1:54322/postgres" > backup_completo.sql
  - backup completo (schema + dados) via container: docker exec supabase_db_260402_crm_cdd pg_dump -U postgres -d postgres > backup_completo.sql
  - Backup físico (volume Docker)
    - Exportar volume para .tar.gz: docker run --rm -v supabase_db_260402_crm_cdd:/data -v "${PWD}:/backup" alpine tar czf /backup/volume_backup.tar.gz -C /data .
    - Limpar volume e restaurar: docker run --rm -v supabase_db_260402_crm_cdd:/data -v "${PWD}:/backup" alpine tar xzf /backup/volume_backup.tar.gz -C /data
  - Restaurar: 
    - psql "postgresql://postgres:postgres@127.0.0.1:54322/postgres" < backup_completo.sql

## supabase CLI

- project dir [260417_supabase_CLI.md](file:///C:/Users/muril/OneDrive/01%20mycloud/01%20sistMu/20.01%20obsidianPkm/20%20km_ssg/10_info_km_ssg/15%20data_mng/260417_supabase_CLI.md)
- start
  - supabase login
  - supabase init --force
  - supabase link --project-ref mqgbhbnkruzlmbwabnob
- pull: schema do remoto para local: supabase db pull --linked
- push: schema local para remoto: supabase db push --linked
- dump (dados): 
  - sobrescrever
    - limpar dados locais (no psql): TRUNCATE public.contacts, public.companies, sync.master_contacts, sync.google_contacts CASCADE;
    - supabase db dump --linked --data-only > remote_data.sql
    - importar dados: docker exec -i supabase_db_260402_crm_cdd psql -U postgres -d postgres < remote_data.sql
  - adicionar: supabase db dump --linked --data-only --use-copy > dados_novos.sql
- migrations
  - cd dev ; supabase migration new fix_sync_status_crm_updated_at
  - cd dev ; supabase db push --linked --include-all
    - supabase db push --linked --include-all
  - supabase db query "ALTER TABLE staging.google_contacts DISABLE TRIGGER trg_sync_contacts_merged;" --linked
- queries
  - supabase db query --linked "select * from sync.google_contacts;"
  - supabase db query --linked "select * from public.contacts;"
  - supabase db query --linked -o json "select * from staging.contacts_merged;" > dev/260417_supabase_contact.json
  - supabase db query --linked --file supabase/migrations/20260419100000_update_trg_sync_contacts_merged.sql
  - limpar bases banco supabase_crm_cloud (mqgbhbnkruzlmbwabnob)
    - supabase db query --linked "TRUNCATE TABLE sync.google_contacts CASCADE; TRUNCATE TABLE sync.master_contacts CASCADE; TRUNCATE TABLE public.contacts CASCADE; UPDATE sync.session_config SET current_session_at = '1900-01-01'::timestamptz WHERE id = 1;"


# gcloud (ggogle api)
- gcloud init
- gcloud auth print-access-token
- `dev\config\260417_google_api_people_get.ps1` para autenticar
- gcloud auth application-default login --client-id-file="dev\config\client_secret.json" --scopes="https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/contacts,profile"

## ativação chave api gemini [aistudio.google](https://aistudio.google.com/api-keys)
```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: AIzaSyD5IqlnTeWbW5odjzAQ_QfN2EtkCgrh0Mw' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
```

## listar modelos disponiveis
```powershell
$key = "AIzaSyD5IqlnTeWbW5odjzAQ_QfN2EtkCgrh0Mw"
$url = "https://generativelanguage.googleapis.com/v1beta/models?key=$key"
$models = Invoke-RestMethod -Uri $url -Method Get
$models.models | Select-Object name, supportedGenerationMethods
```


## request direta API People

### get contacts
```powershell
$TOKEN = $(gcloud auth application-default print-access-token); `
curl.exe -X GET "https://people.googleapis.com/v1/people/me/connections?personFields=names,metadata,photos" `
--header "Authorization: Bearer $TOKEN" --header "Accept: application/json" -o test/test_sessions/curl.json
```

### batchCreateContacts
```powershell
$TOKEN = $(gcloud auth application-default print-access-token); `
curl.exe -X POST "https://people.googleapis.com/v1/people:batchCreateContacts" `
  --header "Authorization: Bearer $TOKEN" `
  --header "Content-Type: application/json" `
  --data "@test\test_sessions\batchCreateContact.json" -o test/test_sessions/curl.json;
```

### batchDeleteContacts
```powershell
$TOKEN = $(gcloud auth application-default print-access-token); `
curl.exe -X POST "https://people.googleapis.com/v1/people:batchDeleteContacts" `
  --header "Authorization: Bearer $TOKEN" `
  --header "Content-Type: application/json" `
  --data "@test\test_sessions\batchDeleteContact.json";
```

### batchUpdateContacts
```powershell
$TOKEN = $(gcloud auth application-default print-access-token); `
curl.exe -X POST "https://people.googleapis.com/v1/people:batchUpdateContacts" `
  --header "Authorization: Bearer $TOKEN" `
  --header "Content-Type: application/json" `
  --data "@test\test_sessions\batchDeleteContact.json";
```

## google sheets cli

### Comandos de edição disponíveis

| Comando              | O que faz                                                            |
| -------------------- | -------------------------------------------------------------------- |
| `values update`      | Edita células existentes (substitui valores em um range)             |
| `values append`      | Adiciona linhas no final                                             |
| `values batchUpdate` | Edita múltiplos ranges de uma vez                                    |
| `values clear`       | Limpa células                                                        |
| `values batchClear`  | Limpa múltiplos ranges                                               |
| `batchUpdate`        | Altera estrutura: add/remove sheet, formatação, merge, redimensionar |
| `sheets copyTo`      | Copia uma sheet para outra planilha                                  |

**Exemplos práticos** (com token renovado):

```powershell
# Editar célula específica
gws sheets spreadsheets values update `
  --params "{"""spreadsheetId""": """ID""", """range""": """Página1!B2""", """valueInputOption""": """USER_ENTERED"""}" `
  --json "{"""values""": [["""100"""]]}"

# Editar múltiplos ranges (batchUpdate values)
gws sheets spreadsheets values batchUpdate `
  --params "{"""spreadsheetId""": """ID""", """valueInputOption""": """USER_ENTERED"""}" `
  --json "{"""data""": [{"""range""": """Página1!A1""", """values""": [["""Novo"""]]}, {"""range""": """Página1!B1""", """values""": [["""Valor"""]]}]}"

# Formatar cabeçalho em negrito (batchUpdate estrutura)
gws sheets spreadsheets batchUpdate `
  --params "{"""spreadsheetId""": """ID"""}" `
  --json "{"""requests""": [{"""repeatCell""": {"""range""": {"""sheetId""": 0, """startRowIndex""": 0, """endRowIndex""": 1}, """cell""": {"""userEnteredFormat""": {"""textFormat""": {"""bold""": true}}}, """fields""": """userEnteredFormat.textFormat.bold"""}}]}"

# Limpar range
gws sheets spreadsheets values clear `
  --params "{"""spreadsheetId""": """ID""", """range""": """Página1!C1:C10"""}"
```

# atomic-crm
- start: `npx vite --host`


# meta api

```powershell
$env:FB_TOKEN = (Get-Content .env | Where-Object { $_ -match '^FB_ACCESS_TOKEN=' }) -replace '^FB_ACCESS_TOKEN=', ''
curl.exe -s -o raw.json "https://graph.facebook.com/v25.0/me?fields=id,name,posts&access_token=$env:FB_TOKEN"
cmd /c "jq . raw.json > curl_formatado.json"
```

## publicar video 

```powershell
curl.exe -i -X POST "https://graph.facebook.com/v25.0/112947826794047/videos" `
  -F "access_token=EAATD3MwZAKbEBRo0E9eDl9fUDtQfTgBZCSkjxqATnZBHiyV6EeAQ9rbMeDkbOuZBpp9LTFfnDHHvCM8aezMMUsM1ZBqWPnAoYsXVw9BJpCkGIBtAzIWhpx0kkIxuZAZB5nJI57x6isvj6xJoY1FhXPqoJxMyHQoxOfD6ZB3agDiNCqcPZAJQQM2mDWbNc6WfVNEZCjhSfL6MdXXnOxfzjiaRcj1nHVT14MZAOQCQyxeZA3lKCPGhzMLUfVLd3iTujQZDZD" `
  -F "no_story=true" `
  -F "title=VIDEO_TITLE" `
  -F "description=What a beautiful day! #sunnyand75" `
  -F "source=@C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\src\assets\post_test\20260516_104319_17906798940410726_VIDEO.mp4"
```
  -F "fbuploader_video_file_chunk=@C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\src\assets\post_test\20260516_104319_17906798940410726_VIDEO.mp4"


```powershell
$headers = @{
    "Authorization" = "OAuth EAATD3MwZAKbEBRo0E9eDl9fUDtQfTgBZCSkjxqATnZBHiyV6EeAQ9rbMeDkbOuZBpp9LTFfnDHHvCM8aezMMUsM1ZBqWPnAoYsXVw9BJpCkGIBtAzIWhpx0kkIxuZAZB5nJI57x6isvj6xJoY1FhXPqoJxMyHQoxOfD6ZB3agDiNCqcPZAJQQM2mDWbNc6WfVNEZCjhSfL6MdXXnOxfzjiaRcj1nHVT14MZAOQCQyxeZA3lKCPGhzMLUfVLd3iTujQZDZD"
    "offset" = "0"
    "file_size" = "463657"
}
$fileBytes = [System.IO.File]::ReadAllBytes("C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\src\assets\post_test\20260516_104319_17906798940410726_VIDEO.mp4")
Invoke-RestMethod -Uri "https://rupload.facebook.com/video-upload/v25.0/973394948777459" `
    -Method Post `
    -Headers $headers `
    -ContentType "application/octet-stream" `
    -Body $fileBytes
```

```powershell
curl.exe -i -X POST "https://graph.facebook.com/v25.0/112947826794047/video_reels" `
  -F "access_token=EAATD3MwZAKbEBRo0E9eDl9fUDtQfTgBZCSkjxqATnZBHiyV6EeAQ9rbMeDkbOuZBpp9LTFfnDHHvCM8aezMMUsM1ZBqWPnAoYsXVw9BJpCkGIBtAzIWhpx0kkIxuZAZB5nJI57x6isvj6xJoY1FhXPqoJxMyHQoxOfD6ZB3agDiNCqcPZAJQQM2mDWbNc6WfVNEZCjhSfL6MdXXnOxfzjiaRcj1nHVT14MZAOQCQyxeZA3lKCPGhzMLUfVLd3iTujQZDZD" `
  -F "video_id=973394948777459" `
  -F "upload_phase=finish" `
  -F "no_story=true" `
  -F "description=What a beautiful day! #sunnyand76"
```
  -F "published=true" `
  -F "video_state=PUBLISHED" `

## publicar video reels

```powershell
curl.exe -i -X POST "https://graph.facebook.com/v25.0/112947826794047/video_reels" `
  -F "access_token=EAATD3MwZAKbEBRo0E9eDl9fUDtQfTgBZCSkjxqATnZBHiyV6EeAQ9rbMeDkbOuZBpp9LTFfnDHHvCM8aezMMUsM1ZBqWPnAoYsXVw9BJpCkGIBtAzIWhpx0kkIxuZAZB5nJI57x6isvj6xJoY1FhXPqoJxMyHQoxOfD6ZB3agDiNCqcPZAJQQM2mDWbNc6WfVNEZCjhSfL6MdXXnOxfzjiaRcj1nHVT14MZAOQCQyxeZA3lKCPGhzMLUfVLd3iTujQZDZD" `
  -F "upload_phase=start"
```

```powershell
$headers = @{
    "Authorization" = "OAuth EAATD3MwZAKbEBRo0E9eDl9fUDtQfTgBZCSkjxqATnZBHiyV6EeAQ9rbMeDkbOuZBpp9LTFfnDHHvCM8aezMMUsM1ZBqWPnAoYsXVw9BJpCkGIBtAzIWhpx0kkIxuZAZB5nJI57x6isvj6xJoY1FhXPqoJxMyHQoxOfD6ZB3agDiNCqcPZAJQQM2mDWbNc6WfVNEZCjhSfL6MdXXnOxfzjiaRcj1nHVT14MZAOQCQyxeZA3lKCPGhzMLUfVLd3iTujQZDZD"
    "offset" = "0"
    "file_size" = "463657"
}
$fileBytes = [System.IO.File]::ReadAllBytes("C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\src\assets\post_test\20260516_104319_17906798940410726_VIDEO.mp4")
Invoke-RestMethod -Uri "https://rupload.facebook.com/video-upload/v25.0/973394948777459" `
    -Method Post `
    -Headers $headers `
    -ContentType "application/octet-stream" `
    -Body $fileBytes
```

```powershell
curl.exe -i -X POST "https://graph.facebook.com/v25.0/112947826794047/video_reels" `
  -F "access_token=EAATD3MwZAKbEBRo0E9eDl9fUDtQfTgBZCSkjxqATnZBHiyV6EeAQ9rbMeDkbOuZBpp9LTFfnDHHvCM8aezMMUsM1ZBqWPnAoYsXVw9BJpCkGIBtAzIWhpx0kkIxuZAZB5nJI57x6isvj6xJoY1FhXPqoJxMyHQoxOfD6ZB3agDiNCqcPZAJQQM2mDWbNc6WfVNEZCjhSfL6MdXXnOxfzjiaRcj1nHVT14MZAOQCQyxeZA3lKCPGhzMLUfVLd3iTujQZDZD" `
  -F "video_id=1285945023714679" `
  -F "upload_phase=finish" `
  -F "no_story=true" `
  -F "description=What a beautiful day! #sunnyand81"
```
  -F "video_state=PUBLISHED" `
  -F "published=true" `
  -F "secret=true" `
  -F "video_state=PUBLISHED" `  [DRAFT, PUBLISHED, SCHEDULED]

## editar video

```powershell
curl.exe -i -X POST "https://graph.facebook.com/v25.0/973394948777459" `
  -F "access_token=EAATD3MwZAKbEBRo0E9eDl9fUDtQfTgBZCSkjxqATnZBHiyV6EeAQ9rbMeDkbOuZBpp9LTFfnDHHvCM8aezMMUsM1ZBqWPnAoYsXVw9BJpCkGIBtAzIWhpx0kkIxuZAZB5nJI57x6isvj6xJoY1FhXPqoJxMyHQoxOfD6ZB3agDiNCqcPZAJQQM2mDWbNc6WfVNEZCjhSfL6MdXXnOxfzjiaRcj1nHVT14MZAOQCQyxeZA3lKCPGhzMLUfVLd3iTujQZDZD" `
  -F "publish_to_news_feed=true"
  ```
  -F "published=true"
  -d "video_state=PUBLISHED"
  -d "secret=true"
  -d "publish=true"
  -d "no_story=false"
  -d "privacy={value:SECRET}"




# understand-anything

$env:GRAPH_DIR = "C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\historico\260614_painel_controle\260511_meta_api_dev\260623_01\src"
cd C:\Users\muril\.understand-anything\repo\understand-anything-plugin\packages\dashboard
npx vite --host 0.0.0.0 --open

http://192.168.1.2:5173/?token=868f48b14c46a21e055c3168e5da2f00


c:\users\muril\venvs\pessoal\Scripts\pyreverse.exe -o dot -p meuprojeto "C:\Users\muril\OneDrive\01 mycloud\01 sistMu\10.01 scripts\01_root\main\260511_meta_api\dev\src"