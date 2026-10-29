# Integrações em uso — G-Click, Metricool, Google Drive

- IA de origem: Claude (conectores MCP configurados na conta)
- Maturidade: Em uso / parcial
- Levantado em: 29/10/2026

## G-Click (Omie.G-Click)
- **O que é hoje**: controle de **obrigações e tarefas** do Escritório TM.
- **Conceitos que precisam sobreviver na migração**:
  - **Vencimento** = prazo **legal** da obrigação; **Meta** = prazo **interno** do escritório (antes do vencimento).
  - **Carteira**: qual colaborador atende qual cliente.
  - **Fluxos de trabalho** (ex.: entrada de cliente).
  - **Painel de pendências**: atrasadas / vencendo na semana.
- **Conector** (somente leitura): `gclick_painel_pendencias`, `gclick_listar_tarefas`, `gclick_detalhar_tarefa`, `gclick_buscar_clientes`, `gclick_listar_clientes`, `gclick_carteira`, `gclick_listar_fluxos`.
- **Status em 29/10/2026**: a API recusou as credenciais (**HTTP 401**). É preciso revisar `GCLICK_CLIENT_ID` e `GCLICK_CLIENT_SECRET` em *Configurações > API* do G-Click. Sem isso não foi possível exportar clientes, carteira e fluxos para o mapeamento.

## Metricool
- Agendamento e análise de Instagram e Facebook. Marca "Escritório TM" `blogId 7336581`, fuso `America/Sao_Paulo`. Alfa BPO ainda não conectada.
- Detalhes de uso em `fontes-originais/tm-social/skills/criar-post/references/metricool.md`.

## Google Drive
- Drive compartilhado **"Escritório TM (novo)"**; marketing em `Marketing › Redes Sociais › [Marca] › AAAA-MM-DD Tema`.
- Limitação: o conector não sobe imagens grandes (base64); as imagens são enviadas pelo app do Drive ou por pasta sincronizada.
- Conta do Drive ligada ao Metricool: contato@escritoriotm.com.br.

## Outros conectores presentes na conta
Gmail, Google Calendar, Google Docs, Slack e o kit Twilio. O kit Twilio pode servir de base para WhatsApp e SMS do agente. Ainda não foi confirmado se algum deles é sistema contratado que precisa ser substituído.

## 14. Aproveitamento na Central RISE
- **G-Click é o principal candidato a substituição** e o mais difícil: a RISE tem tarefas, tarefas recorrentes, prazos e responsáveis, mas **não tem calendário fiscal nem matriz de obrigações por regime tributário**. Ver o desenho proposto em `../consolidado/02-mapa-modulos-rise.md` (seção "Rotinas e obrigações").
- **Antes de desligar o G-Click**: exportar clientes, carteira, fluxos e histórico de tarefas (assim que a credencial for corrigida, o Claude faz a extração pelo conector).
- **Google Drive**: a RISE pode guardar os arquivos dela no Google Drive (integração nativa nas configurações). Isso mantém o Drive como depósito e a RISE como índice.
