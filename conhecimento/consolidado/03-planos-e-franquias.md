# Planos e franquias de serviço

> Coração da regra de atendimento: **o que cada cliente pode pedir, quanto, em que prazo e o que acontece quando passa do limite.**

## O que já está definido
| Marca | Plano | Escopo | Reunião | Volume incluso | Origem |
|---|---|---|---|---|---|
| Alfa BPO | **Iris** | Operação essencial | Semestral | Até 15 NF/mês | `claude/04` |
| Alfa BPO | **Estela** | Gestão financeira | Trimestral | Até 25 NF/mês | `claude/04` |
| Alfa BPO | **Apolo** | Acompanhamento estratégico | Mensal | 25+ NF/mês | `claude/04` |
| Escritório TM | **a levantar** | — | — | — | exportações das outras IAs |

Preços Alfa BPO: **internos**. Não publicar; podem aparecer só em proposta ou contrato do próprio cliente.

## Modelo de dados proposto (plugin "TM Central")

```
servicos                       -- catálogo único de tudo que o cliente pode pedir
  id, codigo, nome, marca (TM|ALFA), categoria (fiscal|dp|legalizacao|documento|bpo|consultoria|duvida)
  tipo_ticket_id (RISE)        -- que tipo de ticket abre
  item_id (RISE)               -- item usado para cobrar avulso/excedente
  preco_avulso, sla_horas_uteis
  atendimento (agente_resolve | agente_abre_humano_executa | so_humano)

planos
  id, marca, nome, item_id (RISE, para a assinatura), ativo
  nivel (1..n)                 -- prioridade na fila e SLA
  canais                       -- whatsapp, email, portal, telefone, presencial
  horario_atendimento_humano

plano_franquias
  plano_id, servico_id
  quantidade                   -- NULL = ilimitado · 0 = não incluso · N = limite
  periodo                      -- mensal | trimestral | semestral | anual | contrato
  regra_excedente              -- cobrar_avulso | pedir_aprovacao | bloquear

contratos_plano                -- vínculo do cliente ao plano
  client_id (RISE), plano_id, contrato_id/subscription_id (RISE)
  inicio, fim, status (ativo | suspenso_inadimplencia | cancelado)
  franquias_extras (json)      -- negociação específica do cliente

consumo_franquia
  id, client_id, servico_id, periodo_ref (ex.: 2026-10)
  quantidade, status (reservado | consumido | estornado)
  ticket_id / task_id (RISE), registrado_por (agente | usuario_id), criado_em
```

## Regras propostas (para decidir)
1. **Quando conta**: reserva ao abrir a demanda, consome ao concluir, estorna se for cancelada pelo escritório. *(decisão aberta: D-A04)*
2. **Período**: franquia mensal não acumula para o mês seguinte. *(decisão aberta: D-A05)*
3. **Excedente**: o agente informa que o limite do período foi atingido, mostra o preço avulso do serviço e pede confirmação explícita do cliente. Com o "sim", abre a demanda e gera a cobrança avulsa (fatura ou item na próxima fatura).
4. **Não incluso no plano**: o agente informa, oferece o serviço avulso e, se fizer sentido, encaminha ao comercial uma proposta de **upgrade** (lead/oportunidade na RISE). Nunca condicionar benefício legal (ex.: gratuidades do MEI) a plano (CDC art. 39 I; LC 123/2006 art. 18 §22-B).
5. **Inadimplência**: contrato `suspenso_inadimplencia` → o agente atende só dúvidas e a regularização financeira e encaminha o restante ao financeiro. *(decisão aberta: D-A06)*
6. **Transparência**: o cliente pode perguntar "quanto ainda tenho este mês?" e o agente responde com o saldo de cada franquia.

## Para levantar (Escritório TM)
- Nomes dos planos, preços e público (MEI, Simples serviço, Simples comércio, Presumido…).
- Por plano: quantos funcionários na folha, quantas notas, quais documentos sob demanda (declarações, recibos, IRPF de sócios?), alterações contratuais/ano, reuniões, canais e horário.
- Tabela de serviços avulsos com preço.
