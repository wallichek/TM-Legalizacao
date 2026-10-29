---
name: planejar-semana
description: "Monta a pauta semanal de publicações do Escritório TM e da Alfa BPO a partir dos resultados do Metricool, do calendário fiscal e de notícias oficiais, e prepara os briefings para a skill criar-post. Use quando o usuário disser \"planejar a semana\", \"pauta da semana\", \"o que vamos postar\", \"resultados da semana\", \"calendário de posts\" ou \"/planejar-semana\".\n"
metadata:
  version: "0.1.0"
---

# Pauta semanal

1. Leia `../criar-post/references/marcas.md`, `../criar-post/references/regras.md` e `../criar-post/references/metricool.md`.
2. Pergunte (uma vez só) a marca — Escritório TM, Alfa BPO ou ambas — e quantos posts por marca (padrão: 2 por semana por marca, espaçados de 2–3 dias).
3. Acione o agente **tm-analista** para os resultados dos últimos 7 dias e os melhores horários da semana seguinte.
4. Liste os posts já agendados no Metricool para a semana seguinte (não duplicar tema nem horário).
5. Monte a pauta: para cada post, data/hora, marca, tema, formato (institucional ou post-rede-social), ângulo, CTA e por que agora (prazo, notícia, desempenho). Priorize prazos legais próximos.
6. Mostre a pauta ao usuário numa tabela e peça aprovação. Ajuste o que ele pedir.
7. Com a pauta aprovada, ofereça iniciar o primeiro post com a skill **criar-post**, já com o briefing preenchido. Crie um post por vez — cada um passa pelas duas aprovações.
