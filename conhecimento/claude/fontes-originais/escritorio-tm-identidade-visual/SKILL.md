---
name: "escritorio-tm-identidade-visual"
description: "Identidade visual do Escritório TM (logo, cores, tipografia, layouts). Use ao criar qualquer peça visual do escritório: post, story, carrossel, capa, apresentação, landing page, banner, design ou HTML."
---

# Identidade visual — Escritório TM

Sistema de marca do **Escritório TM — Contabilidade Inteligente** (Tony Wallichek Lopes, Contador). Toda peça visual voltada a cliente sai nesta identidade. Esta skill é a fonte única: cores, fontes, o símbolo em vetor e os padrões de layout estão aqui, prontos para colar.

Documentos formais (declaração, recibo, ofício, parecer, relatório em papel timbrado) são da skill `escritorio-tm-documentos`; ela já embute esta identidade no gerador DOCX.

## Fluxo

1. **Escolha o formato** na tabela de formatos e fixe o tamanho exato da peça antes de desenhar.
2. **Monte com os tokens desta skill**: cores e fontes da seção Tokens, símbolo da seção Logo (cole o SVG, nunca redesenhe nem use imagem rasterizada).
3. **Aplique um padrão de layout** (seção Padrões). Toda peça leva pelo menos um elemento de assinatura: recorte diagonal navy com filete dourado, fio dourado sob o título, ou motivo de crescimento.
4. **Confira renderizando** a peça e olhando a imagem: logo nítido e inteiro, texto dentro da área segura, contraste conforme a seção Contraste, nenhum texto de exemplo ("[...]") esquecido sem aviso ao usuário. Para avatar e ícones, olhe também em tamanho reduzido (44–80 px).

## Tokens

### Cores

| Token | HEX | Uso |
|---|---|---|
| Azul Navy | `#0D1B36` | Cor primária: fundos escuros, títulos, o "T" do símbolo |
| Navy claro | `#1C3360` | Só em brilho radial sobre fundo navy (centro do gradiente) |
| Dourado | `#D4A017` | Destaque: o "M", filetes, fios, ícones, formas, texto sobre navy |
| Dourado escuro | `#8A6A0E` | Texto dourado pequeno sobre fundo claro (rótulos, eyebrows) |
| Off-white | `#FBFAF7` | Fundo claro padrão |
| Creme | `#F4F2EC` | Painéis e cartões sobre o off-white |
| Branco | `#FFFFFF` | Cartões, texto sobre navy, símbolo negativo |
| Tinta | `#1D2638` | Texto corrido sobre claro |
| Cinza texto | `#3A4458` | Texto de apoio sobre claro |
| Cinza médio | `#6A7384` | Legendas sobre claro |
| Cinza claro | `#C9D1E0` | Texto de apoio sobre navy |
| Borda | `#E6E1D6` | Bordas finas de cartões |

Proporção de uso: navy ~60%, neutros ~30%, dourado ~10%. O dourado é tempero: filetes, fios, uma palavra, um ícone.

CMYK para gráfica: Navy 76/50/0/79 · Dourado 0/25/89/17.

### Contraste

- Branco sobre navy 17:1 e dourado sobre navy 7,2:1: livres para qualquer tamanho.
- Dourado `#D4A017` sobre claro dá só 2,3:1: use para formas, filetes, ícones grandes e o "TM" do logo. Texto dourado sobre claro usa `#8A6A0E` (4,85:1).
- Navy sobre dourado 7,2:1: válido para texto em faixas e cartões dourados.

### Tipografia

Família única: **Montserrat** (Google Fonts). Carregar: `https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap`.

| Papel | Peso | Detalhe |
|---|---|---|
| Chamada, título de capa | 800 | `line-height` 1.04–1.1, `letter-spacing` -0.01em |
| Título | 700 | |
| Subtítulo, rótulo, @handle | 600 | |
| Wordmark "ESCRITÓRIO" | 500 | caixa alta, `letter-spacing` .13em |
| Texto corrido | 400 | `line-height` 1.5–1.7 |
| Eyebrow (rótulo acima do título) | 700 | caixa alta, 11–16 px, `letter-spacing` .24–.30em, dourado |

Em DOCX a fonte é Arial (regra da skill de documentos).

## Logo

### Símbolo (monograma TM)

T em navy; M em dourado formado pela perna esquerda, a diagonal descendente e uma seta ascendente, seguido de três barras crescentes (gráfico). Versão vetorial redesenhada: diagonais paralelas a 49°, barras de largura igual, topos das barras paralelos à seta. Cole exatamente este SVG; ajuste só `width`/`height` mantendo a proporção 670:392 (≈ 1,71:1).

```html
<svg viewBox="405 222 670 392" width="171" height="100" role="img" aria-label="Escritório TM">
  <polygon fill="#0D1B36" points="415,229 750,229 709,298 592,298 592,604 527,604 527,298 415,298"/>
  <polygon fill="#D4A017" points="620,604 620,327 685,327 817.2,478.9 1012.8,254.1 998.2,256 1057.5,232 1041.9,294 1041.8,279.3 801.1,556 681,418 681,604"/>
  <polygon fill="#D4A017" points="883,604 883,499.8 924,452.7 924,604"/>
  <polygon fill="#D4A017" points="944,604 944,429.7 985,382.6 985,604"/>
  <polygon fill="#D4A017" points="1005,604 1005,359.6 1046,312.5 1046,604"/>
</svg>
```

O primeiro polígono é o T; os quatro seguintes formam o M e as barras. Variações trocam só os `fill`:

| Variação | T | M + barras | Fundo |
|---|---|---|---|
| Positiva (padrão) | `#0D1B36` | `#D4A017` | claro |
| Negativa | `#FFFFFF` | `#D4A017` | navy ou foto escura |
| Mono branca | `#FFFFFF` | `#FFFFFF` | dourado, foto |
| Mono navy | `#0D1B36` | `#0D1B36` | carimbo, gravação, 1 cor |
| Mono dourada | `#D4A017` | `#D4A017` | navy (uso decorativo) |
| Marca d'água | mono, `opacity` .05–.06 no claro, .08–.10 no navy | | grande, sangrando a borda |

### Lockups

O wordmark é texto em Montserrat ao lado ou abaixo do símbolo:

- "ESCRITÓRIO" peso 500, `letter-spacing` .13em, na cor do T; "TM" peso 700 em dourado.
- Fio dourado curto (largura ≈ 1,35× a altura das letras do wordmark, espessura ≈ 1/10 dela).
- "CONTABILIDADE INTELIGENTE" peso 500, ≈ 0,36× o tamanho do wordmark, `letter-spacing` .36em.

**Horizontal** — símbolo à esquerda, bloco de texto à direita, `gap` ≈ 0,15× a largura do símbolo; altura do símbolo ≈ altura total do bloco de texto:

```html
<div style="display:flex;align-items:center;gap:24px;font-family:'Montserrat',sans-serif;color:#0D1B36">
  <!-- SVG do símbolo, width="156" height="91" -->
  <div>
    <div style="font-size:31px;font-weight:500;letter-spacing:.13em;white-space:nowrap">ESCRITÓRIO <span style="font-weight:700;color:#D4A017">TM</span></div>
    <div style="width:42px;height:3px;background:#D4A017;margin:10px 0 9px"></div>
    <div style="font-size:11px;font-weight:500;letter-spacing:.36em;white-space:nowrap">CONTABILIDADE INTELIGENTE</div>
  </div>
</div>
```

**Vertical** — mesmo conteúdo empilhado e centralizado; wordmark com largura ≈ 1,3× a do símbolo, espaço entre símbolo e wordmark ≈ 0,08× a largura do símbolo. Para o slogan centralizado, some `padding-left` igual ao `letter-spacing` para compensar o espaço final.

Na versão negativa, texto e T em branco; "TM", fio e M continuam dourados.

### Regras do logo

- Área de proteção: em volta do logo, espaço livre igual à altura do T (a barra horizontal + haste) em todos os lados.
- Tamanho mínimo: logo completo 30 mm / 110 px de largura; abaixo disso, só o símbolo (mínimo 14 mm / 48 px).
- O logo mantém proporção, cor, orientação horizontal e opacidade cheia; sem sombra, contorno ou brilho. Sobre foto, aplique-o numa área limpa ou num cartão.

## Padrões de layout

**Recorte diagonal com filete** (assinatura principal). Painel claro e painel navy separados por uma diagonal inclinada para a direita no topo, com filete dourado de 14–16 px colado à borda. Em CSS, dois `clip-path` sobre um fundo navy:

```css
/* peça 1640×624: painel claro + filete */
.claro  { position:absolute; inset:0; background:#FBFAF7; clip-path:polygon(0 0, 860px 0, 680px 624px, 0 624px); }
.filete { position:absolute; inset:0; background:#D4A017; clip-path:polygon(860px 0, 876px 0, 696px 624px, 680px 624px); }
```

Variação de canto: triângulo navy no canto inferior direito com faixa dourada paralela, para posts e páginas claras.

**Fio dourado sob o título**: barra de 40–110 px × 3–6 px em `#D4A017`, entre o título e o texto de apoio.

**Eyebrow + título + fio + apoio**: a hierarquia padrão de qualquer peça com texto.

**Motivo de crescimento**: barras crescentes em branco com `fill-opacity` .045–.07 e uma curva ascendente dourada com seta (`stroke-opacity` ~.55), no lado navy. Fundos navy podem ganhar um brilho radial `#1C3360` → transparente atrás do conteúdo.

**Arcos dourados**: círculos de borda dourada de 2–3 px com `opacity` .12–.22, sangrando pelos cantos, em capas e stories navy.

**Ícones**: traço (stroke) dourado de 5–5,5 sobre viewBox 100, pontas e junções arredondadas, dentro de círculo navy com anel dourado. Nunca emoji.

## Formatos de redes sociais

Instagram: **@escritoriotm**.

| Peça | Tamanho (px) | Composição |
|---|---|---|
| Foto de perfil | 1080 × 1080 | Fundo navy com brilho radial, anel dourado inset 44 px, símbolo negativo ≈ 62% da largura. Versão branca como alternativa |
| Post do feed | 1080 × 1350 (4:5) | Off-white; logo horizontal no topo esquerdo; eyebrow à direita; título 800 grande; fio; canto diagonal navy + filete; @handle no rodapé; marca d'água TM sangrando |
| Story | 1080 × 1920 | Navy; arcos dourados; símbolo negativo no terço superior; eyebrow + título + fio + apoio; selo em pílula (navy, borda dourada 4 px, símbolo + ponto dourado + @escritoriotm) a ~300 px do rodapé. Deixe ~250 px livres no topo e no rodapé (interface do app) |
| Capa de destaque | 1080 × 1920 | Navy com brilho radial; círculo de borda dourada 760 px centralizado; ícone dourado ou símbolo no centro |
| Capa do Facebook | 1640 × 624 (exportar 2× = 3280 × 1248) | Recorte diagonal: painel claro com logo horizontal à esquerda, navy à direita com eyebrow, chamada, fio e contatos. Área segura: deixe 180 px livres em cada lateral (o celular corta) e o canto inferior esquerdo livre (foto de perfil) |
| Assinatura de post | livre | Símbolo + "@escritoriotm" peso 600, positiva ou negativa |

Carrossel: capa com chamada e "Arraste para o lado →" (seta dourada); slides internos alternando off-white e navy; último slide com logo vertical e contato.

## Conteúdo padrão

- **Contato**: Tony Wallichek Lopes — Contador · CRC PR-068568/O-8 · contato@escritoriotm.com.br · WhatsApp (44) 3244-6971 · www.escritoriotm.com.br
- **Slogan**: CONTABILIDADE INTELIGENTE
- **Posicionamento**: "Contabilidade que impulsiona o crescimento da sua empresa." · pilares Confiança · Organização · Resultados
- **Linha de serviços**: Contabilidade · Fiscal · DP · BPO (completa: contabilidade, fiscal, Departamento Pessoal, BPO financeiro, abertura de empresas, consultoria tributária, planejamento sucessório)
- **Cidade**: Paiçandu/PR
- Texto em português do Brasil, técnico mas acessível ao empresário leigo. Dados que o usuário não forneceu (preço, prazo, número) entram como marcador `[...]` e são apontados na entrega.