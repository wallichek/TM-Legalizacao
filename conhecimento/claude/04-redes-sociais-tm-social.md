# Publicações em redes sociais — plugin tm-social

- IA de origem: Claude (plugin `tm-social`: skills `criar-post`, `planejar-semana`; agentes `tm-pesquisa-legal`, `tm-redator`, `tm-compliance`, `tm-designer`, `tm-publicador`, `tm-analista`)
- Maturidade: Em produção (formato "post de rede social" aprovado em 10/10/2026)
- Marcas: **Escritório TM** (contabilidade) e **Alfa BPO** (BPO financeiro)
- Fonte literal: `fontes-originais/tm-social/`

## 1. Resumo
Pipeline do tema ao post agendado no Metricool: pesquisa em fonte oficial → redação → compliance do texto → **Aprovação 1** (conteúdo técnico, pelo Tony) → artes 1080×1350 → compliance visual → **Aprovação 2** (artes, data, hora) → Drive + agendamento no Metricool. Pauta semanal a partir dos resultados, do calendário fiscal e de notícias oficiais.

## 3. Decisões tomadas
| # | Decisão | Origem |
|---|---|---|
| 1 | Cada publicação pertence a UMA marca; nunca misturar identidade, contato, pasta ou conta | marcas.md |
| 2 | Usar **somente o CRC pessoal do Tony** (CRC PR-068568/O-8) em todos os posts, inclusive ofertas; nunca o CRC da organização | decisão do Tony |
| 3 | Duas aprovações humanas obrigatórias | regras.md |
| 4 | Referências de terceiros nunca são copiadas (só o estilo) | regras.md |
| 5 | Nunca citar concorrentes (ex.: Contabilizei, Conta Azul, Contaja, e-Auditoria) | regras.md |
| 6 | Preços dos pacotes Alfa BPO são **internos**: não publicar sem autorização expressa do Tony | regras.md |
| 7 | Alfa BPO: não agendar enquanto contato e marca no Metricool estiverem pendentes | marcas.md |
| 8 | Horário padrão: dias úteis 10h (2º pico 18h); 2–3 dias entre posts da mesma marca | metricool.md, out/2026 |

## 5. Regras de negócio — Alfa BPO (pacotes)
| Pacote | Escopo | Reunião | Volume |
|---|---|---|---|
| **Iris** | Operação essencial | Semestral | Até 15 NF/mês |
| **Estela** | Gestão financeira | Trimestral | Até 25 NF/mês |
| **Apolo** | Acompanhamento estratégico | Mensal | 25+ NF/mês |

> Primeira definição de **plano com franquia** já existente na base. Ver `../consolidado/03-planos-e-franquias.md`.

## 10. Diretrizes legais (valem para qualquer comunicação ao cliente, inclusive o agente de IA)
- **CFC NBC PG 01**: publicidade informativa, moderada e discreta; sem mercantilização; nome, categoria e nº do CRC em todo anúncio (DL 9.295/46 art. 20).
- **CDC**: a oferta obriga (art. 30); informação clara (art. 31); omissão de dado essencial = publicidade enganosa (art. 37 §3º); venda casada proibida (art. 39 I).
- **CONAR art. 27 §4º**: "grátis" só com custo zero real.
- **MEI**: formalização gratuita por lei; escritório optante pelo Simples faz de graça inscrição, opção pelo SIMEI e 1ª DASN (LC 123/2006, art. 18 §22-B). Tratar como informação, não como promoção.
- **Sem promessas que dependem de terceiros** ("CNPJ em 24h", "aprovação garantida"). Prazo de órgão público = "em média" / "depende do órgão".
- Tom sem urgência artificial ("IMPERDÍVEL", "ÚLTIMA CHANCE").
- Público: empresário leigo (MEI, ME, EPP de Paiçandu, Maringá e região); frases curtas, termo técnico explicado.

## 14. Aproveitamento na Central RISE
- As **diretrizes legais** e de **tom** viram a base do prompt do agente de IA de atendimento (`../consolidado/04-agente-ia-atendimento.md`).
- O padrão "**fonte primária primeiro**" (Receita, Planalto, CGSN, CFC, JUCEPAR, Sefaz-PR) vale para a **base de conhecimento / artigos de ajuda** da RISE que o agente consulta.
- O modelo **ficha + status + aprovações** é o mesmo de um projeto da RISE: o post vira projeto (ou tarefa) com etapas, e as aprovações viram campos ou status.
- O Metricool **não tem equivalente na RISE**: publicar e medir redes sociais está fora do escopo do CRM. Ver `../consolidado/01-inventario-sistemas.md`.
- Pessoas citadas: **Tony** (aprova conteúdo técnico), **Amanda** (acompanha resultados das redes).
