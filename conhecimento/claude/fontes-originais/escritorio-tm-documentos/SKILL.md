---
name: escritorio-tm-documentos
description: >-
  Gera documentos profissionais no papel timbrado oficial do Escritório TM
  (Contabilidade Inteligente) — em DOCX (editável) e PDF (para envio) — a partir
  de um texto que o usuário fornece. Use SEMPRE que o usuário quiser criar,
  redigir, formatar ou "colocar no timbre/papel timbrado" qualquer documento do
  escritório: declaração (de faturamento, de ausência de movimento, de
  enquadramento/EPP, do contador), recibo de pagamento, relatório técnico ou
  contábil, carta/ofício, ofício-circular, parecer, comunicado ou aviso a
  clientes, proposta, ou qualquer peça que deva sair na identidade visual do
  Escritório TM. Dispare mesmo que o usuário não diga "timbre" explicitamente —
  se ele colar um texto e pedir para "formatar", "gerar o documento", "fazer a
  declaração/recibo/ofício" para um cliente, esta skill é a ferramenta certa.
---

# Documentos padronizados — Escritório TM

Esta skill produz documentos na identidade visual do **Escritório TM –
Contabilidade Inteligente** (Tony Wallichek Lopes, Contador). O timbre é uma
imagem de página inteira aplicada no cabeçalho de cada página (logo em cima,
faixa de contatos no rodapé), com margens já ajustadas para o texto nunca
invadir esses elementos. Um gerador em Python (`scripts/tm_gerador.py`) aplica os
estilos padronizados; o timbre-base fica em `assets/TM_base.docx`.

## Fluxo de trabalho

1. **Levante o essencial** com o usuário (se ainda não estiver claro): tipo de
   documento, dados do cliente/empresa (razão social, CNPJ, endereço), número do
   documento (se houver) e o **texto/conteúdo**. Se o usuário anexar um cartão
   CNPJ, extraia os dados dele — mas confira o nome, pois anexos às vezes chegam
   desatualizados; na dúvida, confirme com o usuário.
2. **Prepare o ambiente**: copie `scripts/tm_gerador.py` e `assets/TM_base.docx`
   para o mesmo diretório de trabalho (o gerador procura o timbre-base ao seu
   lado, pela variável `BASE_PADRAO`).
3. **Escreva um pequeno script driver** que importa `TMDoc` e monta o documento
   bloco a bloco (veja a API e o exemplo abaixo). Você identifica as seções,
   monta tabelas quando houver números e aplica destaques nos pontos-chave.
4. **Gere o DOCX** rodando o driver, depois **converta para PDF** com LibreOffice.
5. **Confira** renderizando o PDF em imagem e olhando (garanta que o texto
   respeita o timbre e que a assinatura não quebrou entre páginas).
6. **Entregue** os dois arquivos (DOCX e PDF) ao usuário.

Comandos típicos:

```bash
# a partir do diretório de trabalho, com os dois arquivos já copiados para cá
export PYTHONPYCACHEPREFIX=/tmp/pyc      # evita problemas de cache do Python
python3 -B meu_driver.py                 # gera o .docx
soffice --headless --convert-to pdf saida.docx   # gera o .pdf
pdftoppm -jpeg -r 100 saida.pdf prev     # renderiza para conferência visual
```

## Regras fixas do padrão (não perguntar — já são o padrão)

- **Cidade padrão de emissão: Paiçandu/PR** (o escritório fica em Paiçandu/PR,
  CEP 87140-001). Só use outra cidade se o usuário pedir ou se a natureza do
  documento exigir (ex.: sede do cliente).
- **Assinatura padrão:** o nome do signatário sai sempre em **CAIXA ALTA**
  (o gerador já faz isso automaticamente). Assinatura completa:
  **TONY WALLICHEK LOPES · Contador · CRC PR 068568/O-8**.
- **Identidade visual:** azul-marinho nos títulos/seções, dourado nos detalhes,
  fonte Arial, texto justificado. Tudo isso já está embutido no gerador.
- **Data:** por extenso; se o usuário não informar, use a data do dia.
- Veja `references/preferencias.md` para o registro dessas regras.

## API do gerador (`TMDoc`)

Crie o documento com `d = TMDoc(base="<caminho>/TM_base.docx")` e encadeie os
blocos. Todos os métodos retornam `self`. Métodos disponíveis:

- `rotulo(texto)` — rótulo pequeno dourado acima do título (ex.: "Recibo de Pagamento Nº 001/2026").
- `titulo(texto)` — título principal (marinho, com fio dourado embaixo).
- `subtitulo(texto)` — subtítulo/linha de identificação (cinza itálico).
- `local_data(cidade="Paiçandu/PR", quando=None)` — "Cidade/UF, data por extenso." (alinhado à direita). `quando` aceita um `datetime.date`.
- `saudacao(texto)` — ex.: "A quem possa interessar," / "Prezado(a) cliente,".
- `destinatario([linhas])` — bloco de destinatário (1ª linha em negrito) para cartas/ofícios.
- `referencia(texto)` — linha "Ref.: ...".
- `secao(texto, nivel=1)` — título de seção; `nivel=1` marinho, `nivel=2` dourado menor.
- `paragrafo(texto)` — parágrafo justificado.
- `lista([itens])` — lista com marcador dourado.
- `lista_numerada([itens])` — lista numerada.
- `tabela(cabecalho, linhas, larguras=None)` — tabela com cabeçalho marinho e zebra. `cabecalho` é lista de strings; `linhas` é lista de listas (mesmo nº de colunas); `larguras` (opcional) em cm.
- `destaque(texto)` — faixa de realce com barra dourada à esquerda (ótimo para valores, prazos, conclusões).
- `fecho(texto="Atenciosamente,")` — fecho de correspondência.
- `assinatura(nome="Tony Wallichek Lopes", cargo="Contador", registro="CRC PR 068568/O-8")` — bloco de assinatura (nome em CAIXA ALTA; nunca quebra entre páginas).
- `espaco(pts=8)` — espaçamento vertical.
- `salvar(caminho)` — grava o .docx.

Blocos auxiliares úteis (defina no driver quando precisar), usando os métodos
internos `d._novo_p(...)` e `d._run(...)`:
- "Campo: valor" com rótulo em negrito marinho — para blocos de identificação.
- Alíneas "a) b) c)" — para ressalvas/cláusulas.
- Caixa de valor grande centralizada — para recibos (número grande em marinho entre dois fios dourados).

## Exemplo de driver (recibo de pagamento)

```python
from tm_gerador import TMDoc, NAVY, GOLD, GREY
from docx.enum.text import WD_ALIGN_PARAGRAPH

d = TMDoc(tipo="recibo", base="TM_base.docx")
d.rotulo("Recibo de Pagamento Nº 001/2026")
d.titulo("Recibo de Pagamento")
d.local_data("Paiçandu/PR")

# caixa de valor em destaque
p = d._novo_p(align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=2)
d._run(p, "VALOR", bold=True, size=10, color=GOLD, spacing=40)
d._borda(p, "top", size=8, color="C0801E", space=8)
p = d._novo_p(align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
d._run(p, "R$ 2.280,00", bold=True, size=26, color=NAVY)
p = d._novo_p(align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
d._run(p, "(dois mil, duzentos e oitenta reais)", italic=True, size=11, color=GREY)
d._borda(p, "bottom", size=8, color="C0801E", space=8)

d.paragrafo("Recebemos de EMPRESA X LTDA, CNPJ 00.000.000/0001-00, ..., a importância "
            "de R$ 2.280,00 (dois mil, duzentos e oitenta reais), referente a honorários contábeis.")
d.assinatura()
d.salvar("Recibo.docx")
```

Para uma declaração, troque a estrutura por `saudacao` + `paragrafo`(s) +
`assinatura`. Para relatórios/pareceres, use `secao` numeradas, `tabela` e
`destaque`. Para carta/ofício, use `destinatario` + `referencia` + `saudacao` +
`paragrafo`(s) + `fecho` + `assinatura`.

## Boas práticas

- Sempre **confira o PDF** antes de entregar (renderize e olhe). O texto deve
  ficar dentro das margens do timbre em todas as páginas.
- Ao montar tabelas de valores, **some e confira o total** programaticamente
  antes de escrevê-lo.
- Se um cartão CNPJ indicar um **porte** (ME/EPP) diferente do que o texto do
  documento afirma, avise o usuário — pode haver divergência a corrigir.
- Nomeie os arquivos de saída de forma descritiva (tipo + cliente).
- Entregue **DOCX e PDF**.
