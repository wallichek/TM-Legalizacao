# Visão — Central RISE

> Documento-mãe. Status: **rascunho para aprovação do Tony** (29/10/2026).

## Missão
Ter **um único sistema** para operar o Escritório TM e a Alfa BPO: todo pedido de cliente entra, é atendido, executado, cobrado e medido dentro da Central. Os sistemas de terceiros que hoje fazem partes desse caminho são desligados à medida que a Central cobre a função.

## Plataforma
**RISE – Ultimate Project Manager & CRM** (CodeCanyon, item 15455641), auto-hospedada. A pilha é PHP/CodeIgniter com MySQL, tem **sistema de plugins** para estender sem alterar o núcleo e **portal do cliente** nativo.

## Pilares
1. **Cliente no centro**: cadastro único (empresa, contatos, CNPJ, regime, marca TM/Alfa, plano, carteira/responsável).
2. **Toda demanda é rastreável**: WhatsApp, e-mail, portal ou presencial, tudo vira ticket ou tarefa com tipo, responsável, prazo e status.
3. **Plano manda no atendimento**: o que o cliente pode pedir, quanto e com que prazo vem do plano contratado e das **franquias** dele.
4. **Agente de IA na linha de frente**: atende 24h, identifica o cliente e o plano, resolve o que é informativo, abre e encaminha o que é serviço, controla a franquia e chama um humano quando precisa.
5. **CRM de vendas no mesmo lugar**: lead → proposta → contrato → cliente → onboarding, sem planilha paralela.
6. **Rotina recorrente sob controle**: obrigações mensais e anuais por cliente, com prazo legal (vencimento) e prazo interno (meta).
7. **Conformidade por padrão**: CFC, CDC, CONAR e LGPD aplicados ao atendimento, às propostas e às mensagens do agente.

## Duas marcas, uma central
| | Escritório TM | Alfa BPO |
|---|---|---|
| Serviço | Contabilidade, fiscal, DP, legalização | BPO financeiro |
| Planos | **a levantar** | Iris · Estela · Apolo |
| Identidade | Navy `#0D1B36` + dourado `#D4A017` | Petróleo `#052F4E` + verde `#2DB84B` + dourado |
| Na RISE | Grupo de clientes "Escritório TM" | Grupo de clientes "Alfa BPO" |

Um mesmo cliente pode contratar as duas marcas: um cliente, dois contratos, franquias separadas.

## Arquitetura-alvo (proposta)

```
 WhatsApp ─┐                              ┌─ Equipe (painel RISE)
 E-mail ───┼─► Agente de IA ◄──► Plugin "TM Central" ◄──► RISE (MySQL)
 Portal ───┘   (serviço à parte)   (API própria +         ├─ Clientes / Contatos
               - identifica         planos/franquias)      ├─ Leads / Propostas / Contratos
               - consulta plano                            ├─ Tickets / Projetos / Tarefas
               - abre ticket                               ├─ Faturas / Assinaturas
               - consome franquia                          └─ Base de conhecimento
               - escala p/ humano
```

- **RISE** guarda os dados e a operação.
- **Plugin "TM Central"** (desenvolvimento próprio, pelo mecanismo de plugins da RISE): tabelas de planos e franquias, rotinas e obrigações, e uma **API mínima e controlada** para o agente.
- **Agente de IA** (serviço separado): canais, conversa, regras de plano e escalonamento.

## Fases sugeridas
| Fase | Entrega | Desliga |
|---|---|---|
| 0 | Base de conhecimento consolidada (esta pasta) + decisões abertas respondidas | — |
| 1 | RISE instalada, identidade aplicada, clientes e contatos migrados, equipe e permissões | — |
| 2 | Tickets + portal do cliente + e-mail; CRM de leads, propostas e contratos | atendimento/CRM atuais |
| 3 | Plugin de planos e franquias; faturas e assinaturas | controle de planos em planilha |
| 4 | Rotinas e obrigações (substituto do G-Click) | G-Click |
| 5 | Agente de IA no WhatsApp com franquias | ferramenta de atendimento atual |

Itens da coluna "Desliga" dependem do inventário (`01-inventario-sistemas.md`).
