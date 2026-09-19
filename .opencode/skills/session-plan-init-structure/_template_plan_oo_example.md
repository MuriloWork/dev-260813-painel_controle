# Plano: Refatorar servico de pagamento (PaymentService)

## Referencias
- pastas e arquivos de planejamento
  - plan_dir: sprints\260901_refactor_payment
  - plan_file_pattern: 260901_plan_payment_{version_number}.md
  - briefing_file: AGENTS.md
  - plan_dir: sprints\260901_refactor_payment
  - investigate_file: 260901_plan_payment_01_investigate.md
  - plan_file: 260901_plan_payment_01.md
  - review_file: 260901_plan_payment_01_review.md
- pastas e arquivos de trabalho
  - session_base_dir: src\
    - oop_script: src\scripts\
    - banco: (nao aplicavel)
    - sql_script_dir: (nao aplicavel)
  - session_inicial_version_dir: src\services\

## Funcoes de Negocio
- processar pagamento: recebe pedido, valida cartao, debita, notifica
- estornar pagamento: busca transacao original, reverte debito, notifica
- consultar extrato: lista transacoes por periodo com status

## Estruturas Encontradas

### Arquivos Analisados
- `src/services/payment_service.dart`
  - classes: PaymentService, PaymentValidator
  - funcoes: processPayment, refundPayment, getStatement
  - dependencias: user_service.dart, notification_service.dart
- `src/models/payment_model.dart`
  - classes: Payment, Transaction, PaymentMethod
  - dependencias: (nenhuma)
- `src/gateways/payment_gateway.dart`
  - classes: CreditCardGateway, PixGateway
  - funcoes: charge, refund, validate
  - dependencias: payment_model.dart

### Classes e Metodos
- `PaymentService`
  - `processPayment(order)` — valida cartao, debita, salva transacao, notifica
  - `refundPayment(transactionId)` — busca transacao, estorna, salva status
  - `getStatement(userId, start, end)` — filtra transacoes do periodo
- `PaymentValidator`
  - `validateCard(card)` — verifica BIN, data expiracao, CVV
  - `validateLimit(amount, user)` — verifica saldo disponivel

### Dependencias
- `payment_service.dart -> PaymentService.processPayment() -> payment_gateway.dart`
- `payment_service.dart -> PaymentService.refundPayment() -> payment_gateway.dart`
- `payment_service.dart -> PaymentService -> user_service.dart, notification_service.dart`

## Modificacoes propostas
- **PaymentService.extractStatement()**
  - referencia: `tb_ast_func_map_2d.sql` — CROSS JOIN com contagem de ocorrencias no source_text
  - logica: extrair logica de filtro por periodo do getStatement para metodo separado, reutilizavel por relatorios
  - metodos principais: extractStatement(userId, start, end, filters), generateReport(statementData)
- **PaymentGatewayFactory**
  - referencia: `tb_ast_func.sql` — hierarquia por parent_node_id com mapeamento de niveis
  - logica: criar factory que seleciona gateway (credito/pix/boleto) com base no tipo de pagamento, eliminando switch-case espalhado
  - metodos principais: createGateway(paymentType), getSupportedGateways()

## Plano de Acao
> Aguardando aprovacao do usuario.
### Etapa 01 -- Extrair extractStatement() de PaymentService
### Etapa 02 -- Criar PaymentGatewayFactory
### Etapa 03 -- Atualizar chamadas existentes para usar factory
