# Mapa — módulos da RISE × operação TM / Alfa BPO

> Recursos da RISE listados conforme a documentação pública do produto. **Confirmar na versão instalada**: o site da CodeCanyon estava bloqueado na rede desta sessão, então nada aqui foi conferido na página oficial.

| Módulo RISE | Uso na Central | Configuração / extensão |
|---|---|---|
| **Clientes + contatos** | Cadastro único da empresa e das pessoas que falam com o escritório | Campos personalizados: CNPJ, regime (MEI/Simples/Presumido/Real), marca, **plano**, responsável/carteira, telefone WhatsApp de cada contato |
| **Grupos de clientes** | Separar Escritório TM × Alfa BPO; segmentar por regime | Um grupo por marca |
| **Portal do cliente** | Cliente abre demandas, envia documentos, vê faturas, contratos e andamento | Identidade TM; permissões por módulo |
| **Leads** | CRM de vendas (kanban por status, origem do lead) | Status: Novo → Qualificado → Proposta → Negociação → Ganho/Perdido. Origens: Instagram, indicação, site, WhatsApp |
| **Orçamentos / Propostas / Contratos** | Venda do plano e dos serviços avulsos | Modelos com a identidade TM; itens = planos e serviços do catálogo |
| **Itens** | Catálogo de planos e serviços avulsos com preço | Base do catálogo de franquias (`03-planos-e-franquias.md`) |
| **Faturas + Assinaturas** | Honorários recorrentes e cobrança de excedente | Gateway BR (boleto/PIX) via plugin |
| **Tickets** | Toda demanda do cliente (agente, e-mail, portal) | **Tipos de ticket = tipos de serviço** (declaração, recibo, alteração contratual, 2ª via de guia, dúvida…). E-mail via IMAP |
| **Projetos** | Trabalhos com etapas: abertura de empresa, alteração, transformação MEI → LTDA, onboarding, implantação BPO | Projeto-modelo por tipo (clonar projeto) |
| **Tarefas** (kanban, recorrentes, checklists, responsáveis) | Rotina mensal e obrigações | Ver seção abaixo |
| **Equipe, cargos e permissões** | Colaboradores e acessos | Papéis: Sócio/Contador, Analista fiscal, DP, Legalização, BPO, Comercial |
| **Base de conhecimento / Artigos de ajuda** | Respostas oficiais que o agente consulta e que o cliente lê no portal | Regra "fonte primária primeiro" |
| **Eventos / Agenda** | Reuniões de acompanhamento (semestral/trimestral/mensal do plano Alfa) | Sincronizar com o Google Calendar |
| **Anotações, mensagens, avisos** | Comunicação interna | Pode substituir o Slack |
| **Relatórios + painel** | Volume de demandas, SLA, consumo de franquia, funil | Painéis do plugin para franquias |
| **Plugins** | Extensões sem alterar o núcleo | Plugin próprio "TM Central" |

## Rotinas e obrigações (substituto do G-Click)

A RISE não tem calendário fiscal. Proposta:

1. **Tabela de obrigações** no plugin: código, nome (DAS, DCTFWeb, EFD-Reinf, eSocial, DEFIS, DASN-SIMEI, ECD, ECF, folha…), regime(s) a que se aplica, periodicidade, regra de vencimento (ex.: dia 20 do mês seguinte, com ajuste para dia útil), **dias de meta** (antecedência interna).
2. **Perfil fiscal do cliente**: regime, tem funcionários?, tem pró-labore?, município, atividades (serviço/comércio) → define quais obrigações se aplicam.
3. **Geração mensal** (cron da RISE): para cada cliente, criar as tarefas do mês com **prazo = Meta** e campo personalizado **"Vencimento legal"**, atribuídas pela carteira.
4. **Painel de pendências**: atrasadas pela meta, vencendo pelo vencimento legal, por responsável.
5. **Migração**: importar clientes, carteira e fluxos do G-Click (depende da credencial da API).

## Legalização (projetos-modelo)
| Projeto | Etapas |
|---|---|
| Abertura de empresa | documentos → consulta prévia → FCN → minuta (skill contratos) → assinatura → JUCEPAR → CNPJ → inscrições (municipal/estadual) → alvará → entrega |
| Alteração contratual | documentos → FCN → minuta + consolidação → assinatura → JUCEPAR → atualização de cadastros |
| Transformação MEI → LTDA | conferir CCMEI → FCN (022+046) → instrumento de transformação → JUCEPAR → regime tributário |
| Baixa | pendências fiscais → distrato → JUCEPAR → baixa de inscrições |
