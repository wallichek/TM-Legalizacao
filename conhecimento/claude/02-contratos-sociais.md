# Contratos sociais e alterações contratuais (JUCEPAR)

- IA de origem: Claude (skill `contratos-sociais-tm`)
- Maturidade: Em produção (modelos de referência aprovados: Fernandes e Almeida Ltda e RR Radiadores Ltda, out/2026)
- Projeto/sistema: legalização societária
- Fonte literal: `fontes-originais/contratos-sociais-tm/SKILL.md` (inclui o gerador `gerar_contrato.js`)

## 1. Resumo
Redige minutas .docx prontas para protocolo na JUCEPAR: constituição de LTDA, alteração com consolidação e transformação EI/MEI → LTDA, a partir do FCN, do contrato anterior, da consulta prévia (Empresa Fácil) e do cartão CNPJ/CCMEI. O conteúdo jurídico é redigido pela IA; o layout sai de um gerador fixo (Node + `docx`) alimentado por JSON.

## 3. Decisões tomadas
| # | Decisão |
|---|---|
| 1 | Contrato social **não** usa o timbre nem a assinatura do contador (documento da empresa) |
| 2 | Arial 12 em todo o documento, A4, justificado, rodapé "Página X de Y" |
| 3 | Cabeçalho em todas as páginas: título + **razão social anterior** + CNPJ |
| 4 | **Sem NIRE** em nenhum ponto |
| 5 | Atividades excluídas não são listadas; só o objeto novo completo com CNAEs |
| 6 | Data = "Data da Assinatura" do FCN; local e foro = cidade/comarca da sede |
| 7 | RG do Paraná: órgão emissor SESP-PR |
| 8 | Modelo gerado pela JUCEPAR: manter texto, só formatar; apontar correções à parte |
| 9 | Evento 021 sem contrato anterior → perguntar o que muda; nunca inventar |

## 5. Regras de negócio (eventos do FCN)
002 alteração · 021 alteração de dados (comparar FCN × contrato anterior) · 022 nome empresarial · 046 transformação · 051 consolidação · 307 reenquadramento ME → EPP.

## 7. Fluxo
1. Identificar o instrumento → 2. extrair dados (`pdftotext -layout`) → 3. redigir as cláusulas (estrutura fixa I a XIV no consolidado) → 4. montar `dados.json` → 5. gerar e renderizar para conferência → 6. entregar .docx + lista de "pontos para conferir antes do protocolo".

## 14. Aproveitamento na Central RISE
- **Legalização vira projeto-modelo na RISE**: "Abertura de empresa", "Alteração contratual", "Transformação MEI → LTDA", cada um com tarefas-padrão: coleta de documentos → consulta prévia → FCN → minuta (esta skill) → assinatura → protocolo JUCEPAR → deferimento → CNPJ/inscrições → entrega ao cliente.
- **Checklist de documentos do cliente** (FCN, contrato anterior, CCMEI, RG/CPF dos sócios) vira formulário/arquivos do projeto no **portal do cliente**.
- **Itens de serviço com preço** na RISE: constituição, alteração, transformação, baixa. Os planos podem incluir alterações na franquia (ex.: 1 alteração/ano) e cobrar as excedentes.
- A "lista de pontos a conferir" gerada pela skill vira **comentário na tarefa** de revisão antes do protocolo.
