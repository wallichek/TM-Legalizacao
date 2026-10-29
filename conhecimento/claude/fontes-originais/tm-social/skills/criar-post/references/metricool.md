# Metricool e Google Drive

## Horários (conta Escritório TM, dados do Metricool em out/2026)
- Melhor: dias úteis às **10h** (sexta foi o pico). Segundo pico: **18h**.
- Evitar fins de semana e feriados (alcance baixo), exceto avisos urgentes.
- Intervalo entre posts da mesma marca: 2 a 3 dias.
- Para confirmar horários atuais, use a ferramenta de melhor horário do Metricool para a semana desejada.

## Agendamento via conector Metricool
- Ferramenta: criar post agendado (`createScheduledPost`), `blogId` da marca (Escritório TM = `7336581`).
- `publicationDate`: `{dateTime: "AAAA-MM-DDTHH:mm:ss", timezone: "America/Sao_Paulo"}`; a data não pode estar no passado.
- `providers`: `[{"network":"instagram"},{"network":"facebook"}]`.
- `instagramData`: `{"type":"POST"}` — várias imagens viram carrossel. `facebookData`: `{"type":"POST"}`.
- `media`: URLs públicas ou links de arquivos do Google Drive, **na ordem das telas** (01, 02, 03…). O Drive precisa estar conectado dentro do Metricool (conta contato@escritoriotm.com.br).
- `autoPublish`: `true` (publica sozinho) ou `false` (notificação no app para publicar à mão).
- `text`: legenda final. `firstCommentText`: vazio, salvo pedido.
- A resposta traz `plannerUrl` — sempre devolver ao usuário.
- Para conferir/alterar: listar posts agendados da marca no período; para editar, enviar o conteúdo completo do post alterando só o necessário.

## Google Drive
- Base: Drive compartilhado "Escritório TM (novo)" › `Marketing` › `Redes Sociais` › `[Marca]` › `AAAA-MM-DD Tema`.
- Na subpasta: imagens `tema-01.jpg`, `tema-02.jpg`… e o doc `Legenda - Tema` (data, redes, ordem das imagens, legenda).
- **Limitação**: o conector do Drive envia arquivos dentro da chamada (base64) — imagens grandes não sobem por ele. As imagens são subidas pelo usuário (app do Drive) ou por uma pasta local sincronizada (ex.: rclone no Ubuntu).
- A leitura de docs pelo conector pode exibir emojis corrompidos; o arquivo está correto. Para conferir, baixar como texto.
