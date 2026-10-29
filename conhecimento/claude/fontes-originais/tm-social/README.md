# tm-social — publicações do Escritório TM e da Alfa BPO

Orquestrador de redes sociais: do tema ao post agendado no Metricool, com pesquisa em fonte oficial, revisão de ética/CDC/CONAR, artes na identidade da marca e duas aprovações humanas.

## Componentes
| Tipo | Nome | Função |
|---|---|---|
| Skill (orquestrador) | `criar-post` | Conduz o pipeline completo e para nas duas aprovações |
| Skill | `planejar-semana` | Pauta semanal a partir de resultados, calendário fiscal e notícias |
| Agente | `tm-pesquisa-legal` | Confirma dados em fontes primárias e gera `fontes.md` |
| Agente | `tm-redator` | Texto das telas e legenda |
| Agente | `tm-compliance` | Revisão CFC/CDC/CONAR e regras internas (texto e visual) |
| Agente | `tm-designer` | Telas 1080x1350 a partir do modelo + render e conferência automática |
| Agente | `tm-publicador` | Drive (pasta + legenda) e agendamento no Metricool |
| Agente | `tm-analista` | Resultados do Metricool e sugestões de temas |

Referências compartilhadas: `skills/criar-post/references/` (regras, marcas, formatos, metricool, ficha). Modelo de tela: `skills/criar-post/templates/tela.html`. Render: `skills/criar-post/scripts/render.py`.

## Requisitos
- Conectores ativos na conta: **Metricool** e **Google Drive** (no Claude Code, configurados como servidores MCP).
- No Metricool: Google Drive conectado (conta contato@escritoriotm.com.br) para ler as imagens das pastas.
- Para as artes: Python 3 com `playwright` (Chromium) e `pillow`.
- Opcional (Ubuntu): pasta local sincronizada com o Drive (ex.: rclone) para o publicador copiar as imagens sem upload manual.

## Uso
- `/criar-post post sobre [tema] para [marca]` — anexe links, documentos e prints de referência.
- `/planejar-semana` — pauta da próxima semana.
- Claude Code: `claude --agent ...` não é necessário; rode na conversa principal para as aprovações funcionarem.

## Pendências conhecidas
- Alfa BPO: contato (WhatsApp, site, @) e marca no Metricool.