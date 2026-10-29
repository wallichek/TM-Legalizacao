---
name: "contratos-sociais-tm"
description: "Redige contratos sociais, alterações contratuais com consolidação e transformações EI/MEI em LTDA no padrão .docx do Escritório TM, a partir do FCN e do contrato anterior."
---

# Contratos sociais e alterações contratuais — padrão Escritório TM

Gera a minuta em **.docx**, pronta para protocolo na JUCEPAR, sempre no mesmo layout aprovado por Tony (modelos de referência: Fernandes e Almeida Ltda e RR Radiadores Ltda, out/2026). O conteúdo jurídico é redigido por você; o layout sai de um gerador fixo (`gerar_contrato.js`, no fim deste arquivo) alimentado por um JSON.

Contrato social **não** usa o papel timbrado do escritório nem a assinatura do contador — é documento da empresa e dos sócios. Não use a skill `escritorio-tm-documentos` para isso.

## 1. Identifique o tipo de instrumento

| Situação | Instrumento | Título do cabeçalho |
|---|---|---|
| Empresa nova | Contrato social de constituição | CONTRATO SOCIAL DE CONSTITUIÇÃO DE SOCIEDADE EMPRESÁRIA LIMITADA |
| LTDA já existente com mudança | Alteração contratual + contrato consolidado | [ORDINAL] ALTERAÇÃO E CONSOLIDAÇÃO DO CONTRATO SOCIAL |
| EI ou MEI virando LTDA | Instrumento de transformação + contrato consolidado | INSTRUMENTO DE TRANSFORMAÇÃO DE EMPRESÁRIO INDIVIDUAL EM SOCIEDADE EMPRESÁRIA LIMITADA |
| Tony envia modelo gerado pela JUCEPAR | Só formatação | o título do próprio modelo |

**Modelo da JUCEPAR:** manter o texto exatamente como está (inclusive erros de acentuação e redação pluripessoal); ajustar só maiúsculas/minúsculas e formatação. Pode apontar ao final, em uma lista curta, o que mereceria correção — sem alterar.

## 2. Leia os documentos e extraia os dados

Extraia com `pdftotext -layout`. Fontes e o que tirar de cada uma:

- **FCN (Respostas do FCN):** ato e eventos, razão social, CNPJ, capital, quotas, **data da assinatura**, início das atividades, CNAE principal e secundários, objeto, endereço da sede, qualificação completa de cada sócio, administrador e mandato.
- **Contrato anterior / última consolidação e alterações registradas:** objeto, capital e forma de integralização, nome fantasia, cláusulas vigentes, número de alterações já registradas (para o ordinal), data de arquivamento do ato constitutivo.
- **Consulta prévia (Empresa Fácil):** endereço, tipo de unidade, forma de atuação (ex.: atividades fora do estabelecimento).
- **Cartão CNPJ / CCMEI:** razão social atual, data de abertura, situação do enquadramento MEI.

Eventos do FCN já vistos e o que viram no instrumento:
- **002** — ato de alteração.
- **021** — alteração de dados (exceto nome): o FCN **não diz o que mudou**. Compare FCN × contrato anterior (objeto, CNAEs, endereço/CEP, capital, administração, nome fantasia). Se não houver contrato anterior, peça-o ou pergunte ao Tony quais itens mudam antes de redigir.
- **022** — alteração de nome empresarial.
- **046** — transformação (EI/MEI → LTDA).
- **051** — consolidação: incluir o contrato social consolidado completo.
- **307** — reenquadramento de ME como EPP: cláusula de reenquadramento na alteração + cláusula de enquadramento como EPP no consolidado (art. 3º, II, LC 123/2006).

Mudança só de endereço residencial do sócio não é evento: apenas atualize a qualificação.

## 3. Regras fixas do padrão (não perguntar)

- **Arquivo:** .docx, A4, **Arial 12 em todo o documento** (corpo, cabeçalho, tabela e rodapé), texto justificado, rodapé "Página X de Y".
- **Cabeçalho em todas as páginas:** título do instrumento + **razão social anterior à alteração** + **CNPJ**. O corpo começa direto em "Pelo presente instrumento particular:", sem repetir título.
- **Constituição:** cabeçalho com o título e a razão social; deixe `"cnpj": ""` (a empresa ainda não tem CNPJ). O corpo traz preâmbulo ("Resolve(m) constituir uma sociedade empresária limitada, nos termos da Lei nº 10.406/2002, mediante as condições e cláusulas seguintes:") e direto as cláusulas I a XIV da seção 4, com verbos no futuro ("iniciará suas atividades em…").
- **Sem NIRE** em nenhum ponto do instrumento.
- **Data:** a "Data da Assinatura" do FCN, por extenso no fecho. **Local:** cidade da sede ("Maringá - PR, 30 de setembro de 2026"). **Foro:** comarca da sede.
- **Atividades excluídas não são listadas.** Descreva apenas o novo objeto completo e seus CNAEs, marcando principal e secundárias.
- **Maiúsculas:** nomes de sócios e da empresa em MAIÚSCULAS e negrito; títulos de cláusula em MAIÚSCULAS e negrito; endereços, qualificação e demais textos em maiúsculas/minúsculas normais (converta o CAIXA ALTA do FCN). Ex.: "RUA PIONEIRO ARCIVIDI BRUSCHI, 135" → "Rua Pioneiro Arcividi Bruschi, nº 135".
- **Formatos:** CPF 000.000.000-00; CNPJ 00.000.000/0000-00; CEP 00000-000; quotas com ponto de milhar (20.000); valores "R$ 20.000,00 (vinte mil reais)".
- **RG do Paraná:** órgão emissor SESP-PR.
- **Consolidado não pode perder** o que está vigente e não mudou: nome fantasia, forma de integralização do capital, cláusulas próprias da empresa.
- **Gênero e número:** ajuste sócio/sócia, administrador/administradora, o/a, e singular (unipessoal) ou plural (pluripessoal) em todo o texto.

## 4. Estrutura do instrumento

**Preâmbulo**
1. "Pelo presente instrumento particular:"
2. Qualificação de cada sócio: **NOME**, nacionalidade, estado civil (com regime de bens, se casado), profissão, natural de (se conhecido), nascido(a) em dd/mm/aaaa, portador(a) da Carteira de Identidade nº … SESP-PR, inscrito(a) no CPF sob o nº …, residente e domiciliado(a) na cidade de … - UF, na Rua …, nº …, Bairro, CEP: …;
3. Identificação da empresa: "Único sócio da sociedade empresária limitada **EMPRESA**, com sede na …, inscrita no CNPJ sob o nº …, com ato constitutivo arquivado na Junta Comercial do Estado do Paraná em dd/mm/aaaa;" (pluripessoal: "Únicos sócios componentes da sociedade…"). Use o endereço **atual registrado**, não o novo.
4. "Resolve(m), nos termos da Lei nº 10.406/2002 (Código Civil), promover a [ordinal] alteração contratual e a consolidação do contrato social, mediante as condições e cláusulas seguintes:"

**Cláusulas de alteração** — numeradas por extenso (PRIMEIRA, SEGUNDA…), uma por assunto: endereço, nome empresarial, objeto social, capital, administração, entrada/saída de sócio, reenquadramento. A última é sempre:
> CLÁUSULA [N] - DA CONSOLIDAÇÃO — Em razão das alterações acima, o(s) sócio(s) resolve(m) consolidar o contrato social da sociedade, que passa a vigorar com a redação a seguir, ficando sem efeito as disposições anteriores.

**Transformação EI/MEI → LTDA** (eventos 022 + 046): preâmbulo com o titular e a empresa individual ("Titular da empresa individual …, com sede …, inscrita no CNPJ …, com início das atividades em …"), "Resolve, nos termos do § 3º do art. 968 e do § 1º do art. 1.052 da Lei nº 10.406/2002 (Código Civil), transformar seu registro de empresário individual em sociedade empresária limitada unipessoal…"; cláusulas: DA TRANSFORMAÇÃO (sucede em direitos e obrigações, mantém CNPJ e data de início), DO NOME EMPRESARIAL, DO ENDEREÇO, DAS ATIVIDADES ECONÔMICAS, DO TIPO DE UNIDADE E DA FORMA DE ATUAÇÃO (se houver), DO CAPITAL SOCIAL, DA ADMINISTRAÇÃO, DA CONSOLIDAÇÃO. Confira no CCMEI que o enquadramento MEI já terminou.

**Contrato social consolidado** — bloco `secao` com "CONTRATO SOCIAL CONSOLIDADO" e a razão social **nova**, depois as cláusulas em romanos:

- I - DO NOME EMPRESARIAL — "A sociedade gira sob o nome empresarial **X** [, usa a expressão **Y** como nome fantasia] e rege-se por este contrato social e pelas disposições da Lei nº 10.406/2002 aplicáveis às sociedades limitadas."
- II - DA SEDE — endereço + "Parágrafo único. A sociedade poderá, a qualquer tempo, abrir ou fechar filiais ou outras dependências, mediante alteração contratual assinada pelo(s) sócio(s)."
- III - DO OBJETO SOCIAL — objeto por extenso; parágrafo com forma de atuação, se houver; parágrafo com a lista de CNAEs.
- IV - DO INÍCIO DAS ATIVIDADES E PRAZO DE DURAÇÃO — data de início original; prazo indeterminado.
- V - DO CAPITAL SOCIAL — valor, quotas, valor nominal, "totalmente subscrito e integralizado, em moeda corrente do País," + bloco `capital`.
- VI - DA RESPONSABILIDADE — art. 1.052 CC (pluripessoal: "…mas todos respondem solidariamente pela integralização do capital social").
- VII - DA ADMINISTRAÇÃO — quem administra, isoladamente ou em conjunto, poderes, mandato; parágrafo único vedando uso do nome em atividades estranhas e em fianças/avais.
- VIII - DECLARAÇÃO DE DESIMPEDIMENTO DE ADMINISTRADOR — texto padrão (art. 1.011, § 1º, CC).
- IX - DO EXERCÍCIO SOCIAL E DO BALANÇO PATRIMONIAL — ano civil; prestação de contas em 31 de dezembro.
- X - DO PRÓ-LABORE.
- XI - DA DISTRIBUIÇÃO DE LUCROS — balanços intermediários ou intercalares.
- XII - Unipessoal: DO FALECIMENTO OU INTERDIÇÃO DO(A) SÓCIO(A). Pluripessoal: DA RETIRADA OU FALECIMENTO DE SÓCIO (continuidade com herdeiros ou liquidação das quotas) **e** cláusula DA CESSÃO DE QUOTAS (consentimento e direito de preferência dos demais sócios).
- XIII - DO ENQUADRAMENTO COMO MICROEMPRESA / EMPRESA DE PEQUENO PORTE — inciso I (ME) ou II (EPP) do art. 3º da LC 123/2006, e não incidência no § 4º. Omita se a empresa não for ME/EPP.
- XIV - DO FORO — comarca da sede, "com renúncia a qualquer outro, por mais privilegiado que seja."

Renumere os romanos se incluir ou retirar cláusulas.

**Fecho:** "E, por estar(em) de acordo com tudo o que neste instrumento particular foi lavrado, o(s) sócio(s) obriga(m)-se a cumpri-lo e o assina(m) em uma única via, que será destinada ao registro e arquivamento na Junta Comercial do Estado do Paraná." + bloco `assinatura` com cada sócio (cargo: "Sócio Administrador", "Sócia Administradora" ou "Sócio").

## 5. Gere o .docx

1. Copie o gerador do fim deste arquivo para `gerar_contrato.js` na pasta de trabalho. Ele usa o pacote `docx` do npm (já instalado; só rode `npm install docx` se o `require` falhar).
2. Monte `dados.json`:

```json
{
  "arquivo": "Segunda_Alteracao_EMPRESA.docx",
  "cabecalho": { "titulo": "SEGUNDA ALTERAÇÃO E CONSOLIDAÇÃO DO CONTRATO SOCIAL", "empresa": "RAZÃO SOCIAL ANTERIOR LTDA", "cnpj": "00.000.000/0001-00" },
  "blocos": [
    { "tipo": "p", "texto": "Pelo presente instrumento particular:" },
    { "tipo": "p", "texto": "**NOME DO SÓCIO**, brasileiro, ..." },
    { "tipo": "h", "texto": "CLÁUSULA PRIMEIRA - DO ENDEREÇO" },
    { "tipo": "p", "texto": "..." },
    { "tipo": "lista", "itens": ["CNAE nº 0000-0/00 - Descrição (atividade principal)"] },
    { "tipo": "secao", "linhas": ["CONTRATO SOCIAL CONSOLIDADO", "RAZÃO SOCIAL NOVA LTDA"] },
    { "tipo": "capital", "rotulo": "Nome do Sócio",
      "socios": [{ "nome": "NOME DO SÓCIO", "quotas": "20.000", "valor": "20.000,00", "pct": "100,00" }],
      "total": { "quotas": "20.000", "valor": "20.000,00", "pct": "100,00" } },
    { "tipo": "p", "texto": "E, por estar de acordo ...", "manter": true },
    { "tipo": "assinatura", "local_data": "Maringá - PR, 30 de setembro de 2026",
      "assinantes": [{ "nome": "NOME DO SÓCIO", "cargo": "Sócio Administrador" }] }
  ]
}
```

Tipos de bloco: `p` (parágrafo justificado; `**texto**` vira negrito; `"manter": true` prende ao bloco seguinte), `h` (título de cláusula), `lista` (CNAEs), `secao` (separador + títulos centralizados), `capital` (quadro de quotas; `"rotulo": "Nome da Sócia"` quando for o caso), `assinatura` (local/data + uma linha por sócio). Parágrafos de "Parágrafo único." vão como `p` com o rótulo em negrito: `"**Parágrafo único.** A sociedade…"`.

3. Rode e confira:

```bash
node gerar_contrato.js dados.json
soffice --headless --convert-to pdf ARQUIVO.docx   # ou: python <skill docx>/scripts/office/soffice.py --headless --convert-to pdf ARQUIVO.docx
pdftoppm -jpeg -r 70 ARQUIVO.pdf pagina
```

Olhe as páginas renderizadas: cabeçalho com razão social anterior e CNPJ em todas as páginas, quadro de capital inteiro numa página, fecho e assinatura juntos, nada de texto em CAIXA ALTA indevida.

## 6. Entregue

Envie o .docx. Na resposta, em poucas linhas: o que entrou em cada cláusula de alteração (ligado aos eventos do FCN) e uma lista curta de **pontos para conferir antes do protocolo** — divergências entre FCN, contrato anterior e consulta prévia (CEP, bairro, e-mail, telefone, RG), dados que faltaram e qualquer suposição feita (ex.: ordinal da alteração quando não houver histórico completo).

Se o pedido trouxer só o FCN e o evento for 021 sem contrato anterior, pergunte antes o que muda (ofereça como opções as diferenças que você encontrar) — não invente o objeto ou o capital anterior.

## Gerador (`gerar_contrato.js`)

```javascript
// Gerador de contratos sociais — padrão Escritório TM
// Uso: node gerar_contrato.js dados.json
const fs = require('fs');
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, AlignmentType, WidthType,
  BorderStyle, Header, Footer, PageNumber, ShadingType, LevelFormat, VerticalAlign } = require('docx');

const D = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const FONT = 'Arial', SZ = 24; // Arial 12 em todo o documento
const J = AlignmentType.JUSTIFIED, C = AlignmentType.CENTER, R = AlignmentType.RIGHT, L = AlignmentType.LEFT;

// "texto **negrito** texto" -> TextRuns
const runs = (txt, base = {}) => String(txt).split(/(\*\*[^*]+\*\*)/).filter(Boolean).map(s =>
  s.startsWith('**') ? new TextRun({ text: s.slice(2, -2), bold: true, font: FONT, size: SZ, ...base })
                     : new TextRun({ text: s, font: FONT, size: SZ, ...base }));

const border = { style: BorderStyle.SINGLE, size: 4, color: '000000' };
const borders = { top: border, bottom: border, left: border, right: border };
const W = [4426, 1600, 1800, 1200]; // soma 9026 = largura útil
const cell = (text, w, o = {}) => new TableCell({
  width: { size: w, type: WidthType.DXA }, borders, verticalAlign: VerticalAlign.CENTER,
  shading: o.shade ? { fill: 'E7E6E6', type: ShadingType.CLEAR } : undefined,
  margins: { top: 60, bottom: 60, left: 100, right: 100 },
  children: [new Paragraph({ alignment: o.align || L, keepNext: true, keepLines: true,
    children: [new TextRun({ text, bold: !!o.bold, font: FONT, size: SZ })] })] });

function tabelaCapital(b) {
  const rot = b.rotulo || 'Nome do Sócio';
  const head = new TableRow({ cantSplit: true, tableHeader: true, children: [
    cell(rot, W[0], { bold: true, shade: true }), cell('Qtd Quotas', W[1], { bold: true, shade: true, align: C }),
    cell('Valor em R$', W[2], { bold: true, shade: true, align: C }), cell('%', W[3], { bold: true, shade: true, align: C })] });
  const rows = b.socios.map(s => new TableRow({ cantSplit: true, children: [
    cell(s.nome, W[0]), cell(s.quotas, W[1], { align: R }), cell(s.valor, W[2], { align: R }), cell(s.pct, W[3], { align: R })] }));
  const t = b.total;
  const tot = new TableRow({ cantSplit: true, children: [
    cell('TOTAL', W[0], { bold: true }), cell(t.quotas, W[1], { bold: true, align: R }),
    cell(t.valor, W[2], { bold: true, align: R }), cell(t.pct, W[3], { bold: true, align: R })] });
  return [new Table({ width: { size: 9026, type: WidthType.DXA }, columnWidths: W, rows: [head, ...rows, tot] }),
          new Paragraph({ spacing: { after: 80 }, children: [] })];
}

const out = [];
D.blocos.forEach((b, i) => {
  const prox = D.blocos[i + 1];
  const segura = !!prox && ['lista', 'capital'].includes(prox.tipo); // não separa intro de lista/tabela
  switch (b.tipo) {
    case 'p':
      out.push(new Paragraph({ alignment: J, keepNext: segura || b.manter, spacing: { after: 160, line: 300 }, children: runs(b.texto) }));
      break;
    case 'h': // título de cláusula
      out.push(new Paragraph({ keepNext: true, spacing: { before: 240, after: 120 },
        children: [new TextRun({ text: b.texto, bold: true, font: FONT, size: SZ })] }));
      break;
    case 'lista':
      b.itens.forEach(it => out.push(new Paragraph({ alignment: J, numbering: { reference: 'b', level: 0 },
        spacing: { after: 80, line: 300 }, children: runs(it) })));
      break;
    case 'secao': // separador + título centralizado (ex.: CONTRATO SOCIAL CONSOLIDADO / EMPRESA)
      b.linhas.forEach((t, k) => out.push(new Paragraph({ alignment: C, keepNext: true,
        spacing: { before: k === 0 ? 480 : 0, after: k === b.linhas.length - 1 ? 240 : 60 },
        border: k === 0 ? { top: { style: BorderStyle.SINGLE, size: 4, color: '808080', space: 12 } } : undefined,
        children: [new TextRun({ text: t, bold: true, font: FONT, size: SZ })] })));
      break;
    case 'capital':
      out.push(...tabelaCapital(b));
      break;
    case 'assinatura':
      out.push(new Paragraph({ alignment: C, keepNext: true, spacing: { before: 240, after: 1100 }, children: runs(b.local_data) }));
      b.assinantes.forEach((a, k) => {
        const ult = k === b.assinantes.length - 1;
        out.push(new Paragraph({ alignment: C, keepNext: true, keepLines: true, spacing: { after: 0 }, children: runs('_______________________________________') }));
        out.push(new Paragraph({ alignment: C, keepNext: true, spacing: { after: 0 }, children: [new TextRun({ text: a.nome, bold: true, font: FONT, size: SZ })] }));
        out.push(new Paragraph({ alignment: C, keepNext: !ult, spacing: { after: ult ? 0 : 1100 }, children: runs(a.cargo) }));
      });
      break;
    default: throw new Error('Bloco desconhecido: ' + b.tipo);
  }
});

const g = (t, bold) => new TextRun({ text: t, font: FONT, size: SZ, bold });
const cab = D.cabecalho; // razão social e CNPJ ANTERIORES à alteração
const hdr = new Header({ children: [
  new Paragraph({ alignment: C, children: [g(cab.titulo)] }),
  new Paragraph({ alignment: C, children: [g(cab.empresa, true)] }),
  new Paragraph({ alignment: C, spacing: { after: 120 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: '808080', space: 4 } },
    children: [g(cab.cnpj ? 'CNPJ ' + cab.cnpj : '', true)] })] });
const ftr = new Footer({ children: [new Paragraph({ alignment: R, children: [
  g('Página '), new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: SZ }),
  g(' de '), new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: SZ })] })] });

const doc = new Document({
  styles: { default: { document: { run: { font: FONT, size: SZ } } } },
  numbering: { config: [{ reference: 'b', levels: [{ level: 0, format: LevelFormat.BULLET, text: '•',
    alignment: L, style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }] },
  sections: [{ properties: { page: { size: { width: 11906, height: 16838 },
    margin: { top: 2268, bottom: 1134, left: 1701, right: 1134, header: 567, footer: 567 } } },
    headers: { default: hdr }, footers: { default: ftr }, children: out }],
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(D.arquivo, buf); console.log('OK ' + D.arquivo); });
```