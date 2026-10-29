# Base de conhecimento — Central RISE (Escritório TM · Alfa BPO)

Pasta única para reunir **especificações, decisões e diretrizes** produzidas em conversas com diferentes inteligências artificiais, em fases distintas de maturidade, e aproveitar o que for útil na construção da **Central RISE** (RISE – Ultimate Project Manager & CRM).

## Objetivo da Central

A RISE será a **espinha dorsal da operação**: um único sistema para demandas de clientes, atendimento, CRM de vendas, projetos/rotinas e o **agente de IA** que atende cada cliente de acordo com o **plano contratado e as franquias de serviço** desse plano. Sistemas de terceiros contratados hoje devem ser eliminados sempre que a Central cobrir a função (ver `consolidado/01-inventario-sistemas.md`).

## Como a pasta está organizada

```
conhecimento/
├── README.md                  ← este arquivo (índice e status)
├── _modelos/
│   ├── PROMPT-EXPORTACAO.md    ← prompt para colar em cada conversa de outra IA
│   └── modelo-fonte.md         ← formato padrão de cada documento exportado
├── claude/                    ← conhecimento vindo do Claude (skills, plugins, sessões)
│   ├── README.md
│   ├── 01..05-*.md             ← resumos estruturados por assunto
│   └── fontes-originais/       ← cópia literal das skills/plugins (referência)
├── chatgpt/                   ← exportações das conversas no ChatGPT
├── gemini/                    ← exportações das conversas no Gemini
├── outras-ias/                ← uma subpasta por IA (manus/, deepseek/, copilot/…)
└── consolidado/               ← o que vale para a Central RISE (fonte da verdade)
    ├── 00-visao-central-rise.md
    ├── 01-inventario-sistemas.md
    ├── 02-mapa-modulos-rise.md
    ├── 03-planos-e-franquias.md
    ├── 04-agente-ia-atendimento.md
    ├── 05-registro-decisoes.md
    ├── 06-diretrizes-transversais.md
    └── 07-lacunas-e-conflitos.md
```

**Regra de ouro:** a pasta de cada IA guarda o que *aquela conversa* disse, sem editar o mérito. A pasta `consolidado/` guarda o que *nós decidimos* que vale, sempre citando a origem (`[claude/02]`, `[chatgpt/2026-09-12-crm]`…).

## Fluxo de trabalho

1. **Exportar**: em cada conversa antiga (ChatGPT, Gemini, etc.), cole o prompt de `_modelos/PROMPT-EXPORTACAO.md`.
2. **Salvar**: grave a resposta em `conhecimento/<ia>/AAAA-MM-DD-<assunto>.md` (data da conversa original, não da exportação). Anexos (planilhas, PDFs, prints) vão em `conhecimento/<ia>/anexos/`.
3. **Registrar**: acrescente uma linha na tabela de status abaixo.
4. **Consolidar**: peça ao Claude para "consolidar as novas exportações". Ele compara com `consolidado/`, atualiza o registro de decisões e lista conflitos em `07-lacunas-e-conflitos.md` para você decidir.
5. **Decidir**: cada conflito vira uma decisão sua (Tony) registrada em `05-registro-decisoes.md`.

## Status das fontes

| IA | Documento | Assunto | Maturidade | Consolidado? |
|---|---|---|---|---|
| Claude | `claude/01-documentos-timbrados.md` | Documentos no papel timbrado | Em produção | Sim |
| Claude | `claude/02-contratos-sociais.md` | Contratos sociais / JUCEPAR | Em produção | Sim |
| Claude | `claude/03-identidade-visual.md` | Marca Escritório TM | Em produção | Sim |
| Claude | `claude/04-redes-sociais-tm-social.md` | Pipeline de posts + compliance | Em produção | Sim |
| Claude | `claude/05-integracoes-gclick-metricool.md` | G-Click, Metricool, Drive | Em uso / parcial | Sim |
| ChatGPT | — | aguardando exportação | — | — |
| Gemini | — | aguardando exportação | — | — |

Maturidade: **Ideia** → **Especificado** → **Protótipo** → **Em uso / parcial** → **Em produção**.
