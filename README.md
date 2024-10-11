# Sistema Bancário em Python

Bem-vindo ao **Sistema Bancário em Python**! Este projeto faz parte do **Bootcamp Vivo - Python AI Backend Developer**, especificamente do **Módulo 02 - Desafio Sistema Bancário v2**. Ele foi criado com o objetivo de praticar os conceitos de programação em Python, desenvolvendo um sistema bancário simples, mas funcional, com operações essenciais como depósitos, saques e consultas de extrato, além de funções de criação de usuários e contas correntes.

## Funcionalidades

1. **Depositar**  
   Permite a realização de depósitos no saldo da conta. O valor depositado é adicionado ao saldo e registrado no extrato.

2. **Sacar**  
   Realiza saques da conta, respeitando os limites de saldo disponível, limite de saques por transação e um máximo de 3 saques diários.

3. **Extrato**  
   Exibe todas as movimentações financeiras, incluindo depósitos e saques, bem como o saldo atual.

4. **Criar Usuário**  
   Função para cadastro de um novo usuário com nome, CPF (somente números), data de nascimento e endereço completo. Um mesmo CPF não pode ser cadastrado mais de uma vez.

5. **Criar Conta Corrente**  
   Associa uma conta corrente a um usuário já cadastrado. A agência é fixa (`0001`), e o número da conta é gerado automaticamente. Um usuário pode ter mais de uma conta.

6. **Listar Contas**  
   Exibe todas as contas criadas no sistema, listando o número da conta, a agência e o usuário associado.

## Alterações no Menu

Uma das principais mudanças feitas foi a substituição do menu numérico antigo por um menu com letras para facilitar a navegação:

- De:
  - `[1] Depositar`
  - `[2] Sacar`
  - `[3] Extrato`
  - `[4] Limite de Saque por Transação`
  - `[5] Limite de Saques Diários Restantes`
  - `[0] Sair`
  
- Para:
  - `[d] Depositar`
  - `[s] Sacar`
  - `[e] Extrato`
  - `[c] Criar Usuário`
  - `[cc] Criar Conta Corrente`
  - `[l] Listar Contas`
  - `[q] Sair`

Além disso, foram implementadas todas as funcionalidades solicitadas no desafio, como a criação de usuários e contas correntes.

## Como Utilizar

Ao executar o programa, será exibido um menu com as seguintes opções:

- `[d] Depositar`
- `[s] Sacar`
- `[e] Extrato`
- `[c] Criar Usuário`
- `[cc] Criar Conta Corrente`
- `[l] Listar Contas`
- `[q] Sair`

### Exemplo de Fluxo

1. Crie um usuário com a opção `[c] Criar Usuário`.
2. Associe uma conta a esse usuário com a opção `[cc] Criar Conta Corrente`.
3. Realize depósitos, saques e consulte o extrato conforme necessário.

### Validações Implementadas

- **Saques**: São permitidos até 3 saques diários. O valor do saque não pode exceder o saldo disponível ou o limite por transação.
- **Depósitos**: Somente valores positivos são aceitos.
- **Usuários**: Não é permitido cadastrar dois usuários com o mesmo CPF.

## O que Aprendi Até Aqui?

Durante o desenvolvimento deste sistema bancário, aprendi a organizar melhor o código através do uso de funções, além de validar dados de forma mais eficiente. O projeto foi uma excelente oportunidade para praticar conceitos como passagem de argumentos, retornos de função, e a construção de um fluxo lógico que abrange múltiplas funcionalidades de um sistema.
