---
name: criar-post
description: "Orquestra a criação completa de uma publicação para o Instagram e o Facebook do Escritório TM ou da Alfa BPO, da pesquisa ao agendamento no Metricool, coordenando os agentes tm-pesquisa-legal, tm-redator, tm-compliance, tm-designer e tm-publicador, com duas aprovações humanas no caminho. Use esta skill quando o usuário disser \"criar post\", \"criar publicação\", \"fazer um carrossel\", \"post sobre [tema]\", \"publicação para o escritório\", \"post da Alfa BPO\", \"transforme este link/documento em post\" ou \"/criar-post\".\n"
metadata:
  version: "0.1.0"
---

# Orquestrador de publicações (Escritório TM e Alfa BPO)

Coordene os agentes especialistas para levar uma publicação do pedido ao agendamento. Fique na conversa principal: só ela pode pausar e pedir aprovação. Delegue o trabalho pesado aos agentes e mantenha o usuário informado em frases curtas.

## Antes de começar

1. Leia `references/regras.md` e `references/marcas.md`. Releia sempre que houver dúvida: as regras valem em todas as etapas.
2. Se houver um projeto "Marketing" com `CLAUDE.md` acessível, leia-o também. Em conflito, vale o que o usuário disser na conversa; depois, o CLAUDE.md do projeto; depois, estas referências.
3. Monte o **briefing** a partir do pedido. Pergunte de uma vez só (no máximo 3 perguntas) apenas o que faltar e não puder ser inferido:
   - **marca**: Escritório TM ou Alfa BPO (obrigatório; nunca misture);
   - **tema** e material de base (links, documentos anexos, prints de referência);
   - **objetivo**: informar / alertar prazo / oferta de serviço;
   - **formato**: carrossel institucional (padrão) ou "post de rede social" (ver `references/formatos.md`);
   - **nº de telas** (padrão 5 a 7) e **data/hora** desejadas (padrão: próximo dia útil livre às 10h);
   - **CTA**: WhatsApp (padrão), salvar o post ou comentar palavra-chave.
4. Crie a **ficha do post** na pasta de trabalho `posts/AAAA-MM-DD-slug/ficha.md` com o modelo de `references/ficha.md`. Atualize o campo `status` a cada etapa. Todo agente recebe o caminho da ficha e grava seus resultados na mesma pasta.

## Pipeline

Execute as etapas na ordem. Rode em paralelo apenas o que for marcado como paralelo.

### Etapa 1 — Pesquisa (paralelo)
- Chame **tm-pesquisa-legal** com o tema, os links e documentos, a marca e o caminho da ficha. Ele grava `fontes.md` com cada dado técnico, a fonte primária e o status (confirmado / não confirmado).
- Se houver prints de referência, analise-os aqui mesmo (na conversa principal, que vê as imagens) e grave em `referencia.md` apenas **o que funciona no estilo** (formato, ritmo, hierarquia, tipo de CTA). Nunca transcreva textos da referência.

### Etapa 2 — Redação
- Chame **tm-redator** com a ficha, `fontes.md` e `referencia.md` (se houver). Ele grava `telas.md` (texto de cada tela) e `legenda.md`.
- O redator só pode usar dados marcados como confirmados em `fontes.md`.

### Etapa 3 — Compliance do texto
- Chame **tm-compliance** com a pasta do post. Ele grava `compliance.md` com veredito `APROVADO`, `AJUSTAR` ou `BLOQUEADO`.
- `AJUSTAR`: devolva os apontamentos ao tm-redator e repita a etapa 3. Máximo de 2 rodadas; depois disso, leve os pontos ao usuário.
- `BLOQUEADO`: pare e explique ao usuário o motivo (ex.: preço interno da Alfa BPO, promessa que depende de órgão público).

### ⛔ Aprovação 1 — conteúdo técnico
Mostre ao usuário, de forma compacta: o texto de cada tela, a legenda e a lista de fontes. Pergunte se aprova (o Tony aprova conteúdo técnico; registre quem aprovou e quando na ficha). **Não gere artes sem essa aprovação.** Aplique os ajustes pedidos pelo tm-redator e, se o conteúdo técnico mudar, rode a etapa 3 de novo.

### Etapa 4 — Artes
- Chame **tm-designer** com a pasta do post. Ele gera um HTML por tela a partir de `templates/tela.html`, renderiza com `scripts/render.py`, corrige estouros e entrega `jpg/NN.jpg` + `contato.png` (folha com todas as telas).
- Mostre ao usuário a folha de contato (envie o arquivo). Se o ambiente permitir publicar as telas num canvas de design editável, ofereça.

### Etapa 5 — Compliance visual
- Chame **tm-compliance** de novo, agora sobre as imagens/HTML: CRC, contato, condições na arte, nada encostando em faixa, marca certa.

### ⛔ Aprovação 2 — artes, data e hora
Mostre as telas finais, a legenda, a data e a hora propostas (consulte `references/metricool.md` para horários). Pergunte também: publicação **automática** (padrão) ou **com notificação** no app. **Não agende sem essa aprovação.**

### Etapa 6 — Publicação
- Chame **tm-publicador** com a pasta do post, a marca, a data/hora aprovadas e o modo de publicação. Ele:
  1. cria a subpasta no Drive (`Marketing › Redes Sociais › [Marca] › AAAA-MM-DD Tema`) e salva o doc da legenda;
  2. verifica se as imagens estão na subpasta — se não estiverem (o conector do Drive não sobe imagens grandes), informa ao usuário exatamente quais arquivos subir e onde, e **pausa**;
  3. com as imagens no Drive, agenda no Metricool (Instagram carrossel + Facebook) e devolve o link do agendamento.
- Atualize a ficha com `status: agendado`, data/hora e link.

## Encerramento
Responda ao usuário em poucas linhas: o que foi agendado, quando, o link no Metricool e qualquer pendência. Não recapitule as etapas.

## Regras de orquestração
- Passe a cada agente apenas o que ele precisa: caminho da ficha/pasta, marca e a instrução da etapa. Os agentes leem as referências por conta própria.
- Nunca pule as duas aprovações, mesmo se o usuário estiver com pressa — ofereça encurtar o resto, não os portões.
- Se um agente falhar ou voltar sem o arquivo esperado, tente uma vez com instrução mais específica; na segunda falha, informe o usuário e siga com o que for possível.
- Posts urgentes (prazo da Receita, mudança de lei com data): proponha a data mais próxima possível e diga isso no briefing.
- Ao fim, se o usuário pedir, registre a publicação no calendário do projeto (doc de fluxo/handoff).
