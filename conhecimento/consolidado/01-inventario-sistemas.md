# Inventário de sistemas de terceiros × Central RISE

> Preencha as linhas **"a confirmar"** com o que o escritório paga hoje. Cada linha vira uma decisão de desligar, manter ou integrar.

| Sistema atual | Função hoje | Cobertura na RISE | Decisão proposta | Status |
|---|---|---|---|---|
| **G-Click (Omie)** | Obrigações, tarefas, carteira, fluxos | Parcial: tarefas, recorrência, responsáveis e prazos. **Falta** calendário fiscal e matriz de obrigações por regime | **Substituir** na Fase 4, com plugin de rotinas | Em uso; API com 401 |
| **Metricool** | Agendar e medir Instagram/Facebook | **Nenhuma** | **Manter**: fora do escopo de um CRM. Reavaliar só se surgir alternativa que caiba no orçamento | Em uso |
| **Google Drive** | Arquivos do escritório e do marketing | A RISE guarda arquivos e pode usar o Google Drive como armazenamento | **Manter como depósito**; RISE como índice por cliente/projeto | Em uso |
| **Gmail / Google Workspace** | E-mail, agenda, documentos | Não substitui e-mail; a RISE recebe tickets por e-mail (IMAP) e sincroniza eventos com o Google Calendar | **Manter** (infraestrutura) | Em uso |
| **Slack** | Comunicação interna? | A RISE tem mensagens internas e notificações (e integração com Slack) | Avaliar: pode ser substituído pelas mensagens da RISE | a confirmar |
| Ferramenta de atendimento WhatsApp | Atendimento ao cliente | Nenhuma nativa → **agente de IA + API do WhatsApp** | **Substituir** na Fase 5 | a confirmar (qual?) |
| CRM de vendas atual | Leads, funil | Leads (kanban, origens, status), propostas, orçamentos, contratos | **Substituir** na Fase 2 | a confirmar (qual?) |
| Cobrança (boleto/PIX) | Honorários mensais | Faturas e assinaturas nativas; gateways nativos são internacionais (Stripe, PayPal…). **Boleto/PIX exige plugin** de gateway brasileiro | Integrar gateway BR via plugin | a confirmar (qual banco/gateway?) |
| Emissão de NFS-e | Nota dos honorários | **Nenhuma** | Manter emissor atual ou integrar via API (plugin) | a confirmar |
| Assinatura eletrônica | Contratos, propostas | Aceite e assinatura simples de propostas e contratos | Avaliar validade jurídica para cada caso | a confirmar |
| Sistema contábil/fiscal (Domínio, Alterdata, Questor…) | Escrituração, folha, apuração | **Nenhuma** (não é função da RISE) | **Manter** | a confirmar |

## Regras para decidir
1. Só desligar depois de **exportar os dados** e rodar **pelo menos um ciclo mensal** em paralelo.
2. Quando a função não existe na RISE, a preferência é **plugin próprio** (controle total) e não alterar o núcleo da RISE, porque alteração no núcleo se perde a cada atualização.
3. Sistemas de produção contábil (escrituração, folha) **não** entram no escopo da Central.
