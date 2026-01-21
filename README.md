# ERP Funilaria e Pintura

Este repositório contém a base inicial para um ERP voltado a oficinas de funilaria e pintura. A proposta é organizar o fluxo completo da oficina, desde o cadastro de veículos e clientes até a gestão financeira e de estoque.

## Objetivos do sistema

- Centralizar o cadastro de clientes, veículos e seguradoras.
- Controlar orçamentos, ordens de serviço e status de reparo.
- Monitorar estoque de peças e insumos (tinta, verniz, consumíveis).
- Registrar apontamentos de mão de obra e produtividade.
- Consolidar informações financeiras (contas a pagar/receber, faturamento, fluxo de caixa).

## Módulos principais

1. **Cadastro e CRM**
   - Clientes, contatos e seguradoras.
   - Veículos e histórico de atendimentos.

2. **Orçamentos e Ordem de Serviço**
   - Geração de orçamento com itens, mão de obra e peças.
   - Conversão para ordem de serviço e controle de status.

3. **Produção e Controle de Oficina**
   - Checklist de entrada e saída.
   - Etapas do processo (desmontagem, funilaria, pintura, montagem, polimento).

4. **Estoque e Compras**
   - Catálogo de peças e materiais.
   - Alertas de estoque mínimo e pedido de compra.

5. **Financeiro**
   - Contas a pagar e receber.
   - Fluxo de caixa e conciliação.

6. **Indicadores**
   - TMA (tempo médio de atendimento), lead time e retrabalho.
   - Rentabilidade por serviço.

## Próximos passos sugeridos

- Validar os requisitos detalhados com a oficina (processos e formulários).
- Definir o stack tecnológico (ex.: backend Python/Node, frontend React, banco PostgreSQL).
- Implementar autenticação e controle de acesso por perfil.
- Criar um MVP focado em orçamento + ordem de serviço.

## Documentação complementar

- [Mapa de módulos e fluxos](docs/erp-modulos.md)
- [Modelo de dados inicial](database/schema.sql)
- [Rascunho de endpoints](docs/api.md)
