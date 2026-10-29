# Prompt de exportação — colar no fim de cada conversa antiga

Use em cada conversa (ChatGPT, Gemini, Claude.ai, Manus, Copilot, DeepSeek…) que tratou de qualquer parte do projeto: CRM, atendimento, agente de IA, planos/franquias, rotinas contábeis, automações, marketing, documentos, integrações.

Cole o texto abaixo **como mensagem nova dentro da própria conversa** (assim a IA enxerga todo o histórico). Se a conversa for muito longa e a IA cortar a resposta, peça "continue a partir da seção N".

---

```text
Vou centralizar tudo o que construímos nesta conversa numa base de conhecimento única, que será usada para implantar a Central RISE (RISE Ultimate Project Manager & CRM) como sistema único do Escritório TM (contabilidade) e da Alfa BPO (BPO financeiro): demandas de clientes, atendimento, CRM de vendas, projetos/rotinas e um agente de IA que atende cada cliente conforme o plano contratado e as franquias de serviço do plano.

Exporte TODO o conhecimento desta conversa no formato abaixo, em Markdown, em português do Brasil.

Regras:
- Não invente nada. Use apenas o que foi dito ou produzido nesta conversa.
- Separe com clareza o que foi DECIDIDO pelo usuário, o que foi apenas SUGERIDO por você e o que ficou EM ABERTO.
- Reproduza literalmente (em bloco de código) prompts, regras, tabelas, fluxos, modelos de dados, códigos, scripts e textos finais que tenham sido aprovados. Não resuma esses itens.
- Indique datas sempre que aparecerem na conversa.
- Se um assunto não foi tratado, escreva "não tratado" na seção correspondente.

Formato:

# [Título curto do assunto]
- IA de origem: [nome e modelo, se souber]
- Período da conversa: [primeira e última data que você identifica]
- Maturidade: Ideia | Especificado | Protótipo | Em uso / parcial | Em produção
- Projeto/sistema a que se refere: [ex.: agente de WhatsApp, CRM, portal do cliente, rotina fiscal]

## 1. Resumo em 5 linhas
## 2. Objetivo e problema que resolve
## 3. Decisões tomadas (tabela: # | decisão | motivo | data | quem decidiu)
## 4. Especificações funcionais (o que o sistema/processo faz, passo a passo)
## 5. Regras de negócio (planos, franquias, limites, preços, prazos, SLAs, exceções)
## 6. Modelo de dados (entidades, campos, relacionamentos)
## 7. Fluxos e processos (atendimento, vendas, onboarding, rotina mensal, cobrança)
## 8. Agente de IA (persona, tom, escopo, o que pode e não pode fazer, escalonamento para humano, prompts)
## 9. Integrações e sistemas citados (nome, para que serve hoje, se deve ser substituído pela RISE)
## 10. Diretrizes e restrições (legais: CFC, CDC, LGPD; de marca; operacionais)
## 11. Artefatos produzidos (prompts, códigos, planilhas, textos aprovados — literais)
## 12. Sugeridas e não decididas
## 13. Pendências e perguntas em aberto
## 14. O que pode ser aproveitado na Central RISE (sua avaliação, separada do resto)
```

---

## Depois de receber a resposta

1. Salve como `conhecimento/<ia>/AAAA-MM-DD-<assunto>.md`. Use a data da conversa original, não a de hoje. Exemplo: `conhecimento/chatgpt/2026-08-14-agente-whatsapp.md`.
2. Se a conversa tiver arquivos (planilhas de planos, tabelas de preço, PDFs), baixe-os e coloque em `conhecimento/<ia>/anexos/`.
3. Adicione a linha na tabela "Status das fontes" do `conhecimento/README.md`.
4. Peça ao Claude: **"consolide as novas exportações da base de conhecimento"**.
