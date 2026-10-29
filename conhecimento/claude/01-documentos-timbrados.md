# Documentos no papel timbrado do Escritório TM

- IA de origem: Claude (skill `escritorio-tm-documentos`)
- Maturidade: Em produção
- Projeto/sistema: geração de documentos do escritório (DOCX + PDF)
- Fonte literal: `fontes-originais/escritorio-tm-documentos/`

## 1. Resumo
Gera declarações, recibos, relatórios, cartas/ofícios, pareceres, comunicados e propostas no timbre oficial, em DOCX (editável) e PDF (envio). Um gerador Python (`tm_gerador.py`, classe `TMDoc`) aplica estilos fixos sobre o timbre-base `TM_base.docx`.

## 3. Decisões tomadas
| # | Decisão | Motivo |
|---|---|---|
| 1 | Cidade padrão de emissão: **Paiçandu/PR, CEP 87140-001** (não Umuarama) | Sede do escritório; correção registrada |
| 2 | Assinatura: **TONY WALLICHEK LOPES · Contador · CRC PR 068568/O-8**, nome em CAIXA ALTA | Padrão do escritório |
| 3 | Visual: navy nos títulos, dourado nos detalhes, **Arial**, texto justificado | Identidade em DOCX |
| 4 | Data por extenso; se não informada, a do dia | Padrão |
| 5 | Sempre entregar **DOCX e PDF** e conferir o PDF renderizado antes | Qualidade |

## 5. Regras de negócio
- Dados do cliente vindos de cartão CNPJ devem ser conferidos (anexos chegam desatualizados).
- Se o porte (ME/EPP) do cartão CNPJ divergir do texto, avisar.
- Totais de tabelas de valores são somados e conferidos por programa.
- Arquivos nomeados por tipo + cliente.

## 11. Artefatos
- API `TMDoc`: `rotulo`, `titulo`, `subtitulo`, `local_data`, `saudacao`, `destinatario`, `referencia`, `secao`, `paragrafo`, `lista`, `lista_numerada`, `tabela`, `destaque`, `fecho`, `assinatura`, `espaco`, `salvar`.
- Exemplo de driver (recibo) em `fontes-originais/escritorio-tm-documentos/SKILL.md`.

## 14. Aproveitamento na Central RISE
- **Modelos de documento na RISE**: RISE gera PDF de faturas, orçamentos, propostas e contratos a partir de modelos HTML editáveis. Os modelos de **Proposta** e **Contrato de prestação de serviços** devem receber esta identidade (navy/dourado, assinatura do Tony, Paiçandu/PR).
- **Documentos sob demanda do cliente** (declaração de faturamento, recibo, declaração de ausência de movimento) são candidatos a **serviços com franquia** no plano (ver `consolidado/03-planos-e-franquias.md`). O agente de IA pode abrir a demanda; a emissão continua por esta skill até haver gerador dentro da RISE.
- Lista de tipos de documento → vira a lista de **"Tipos de demanda"** (tipos de ticket/tarefa) na RISE.
