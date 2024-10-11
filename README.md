# Sistema Bancário em Python

Bem-vindo ao **Sistema Bancário em Python**! Esse projeto faz parte do **Bootcamp Vivo - Python AI Backend Developer**, mais especificamente do **Módulo 02 - Desafio Sistema Bancário v2**. Ele foi desenvolvido com o objetivo de aprender e aplicar os conceitos de programação em Python, criando um sistema bancário simples, mas funcional. Aqui, vamos gerenciar depósitos, saques, extratos, além de criar usuários e contas correntes.

## Funcionalidades

1. **Depositar**  
   Você pode realizar depósitos no saldo da sua conta. O valor será adicionado ao saldo atual e registrado no extrato.

2. **Sacar**  
   Aqui é onde você pode sacar um valor da sua conta, desde que respeite o limite de saques diários (máximo de 3) e o limite do saldo.

3. **Extrato**  
   Consulta todas as movimentações financeiras feitas na conta, mostrando tanto os depósitos quanto os saques.

4. **Criar Usuário**  
   Cadastramento de um novo usuário no sistema com nome, CPF (somente números), data de nascimento e endereço. Importante: cada CPF pode ter apenas um cadastro.

5. **Criar Conta Corrente**  
   Após criar um usuário, é possível associar uma conta corrente ao mesmo. Cada usuário pode ter mais de uma conta. A agência é fixa: `0001`, e o número da conta é gerado automaticamente.

6. **Listar Contas**  
   Lista todas as contas criadas, mostrando o número da conta, agência e o usuário vinculado.

## Como Utilizar

Ao rodar o programa, será exibido um menu com as opções:

- `[d] Depositar`
- `[s] Sacar`
- `[e] Extrato`
- `[c] Criar Usuário`
- `[cc] Criar Conta Corrente`
- `[lc] Listar Contas`
- `[q] Sair`

### Exemplo de Fluxo

1. Primeiro, crie um usuário com a opção `[c] Criar Usuário`.
2. Depois, associe uma conta a esse usuário com a opção `[cc] Criar Conta Corrente`.
3. Agora, você já pode fazer depósitos, saques e conferir o extrato.

### Validações Implementadas

- **Saques**: Você só pode fazer até 3 saques diários e respeitar o limite do saldo e o valor máximo de saque.
- **Depósitos**: Só aceitamos valores positivos.
- **Usuários**: Não é permitido cadastrar dois usuários com o mesmo CPF.

## O que aprendi até aqui?

Durante o desenvolvimento deste projeto, aprendi a organizar melhor o código usando funções, separar responsabilidades e validar dados de forma mais eficiente. Também foi um ótimo exercício para entender como estruturar um sistema com múltiplas funcionalidades.
