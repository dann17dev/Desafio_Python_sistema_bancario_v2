menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Usuário
[cc] Criar Conta Corrente
[l] Listar Contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato_bancario = ""  # Renomeado
numero_saques = 0
LIMITE_SAQUES = 3

# Ações para criar usuários e contas
usuarios = []  # Lista para armazenar usuários 
contas = []  # Lista para armazenar contas
numero_conta = 1  # contador para número da conta 

# Funções existentes
def depositar(saldo, valor, extrato_bancario):  # Renomeado
    saldo += valor
    extrato_bancario += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato_bancario  # Renomeado

def sacar(*, saldo, valor, extrato_bancario, limite, numero_saques, limite_saques):  # Renomeado
    if valor > saldo:
        return saldo, extrato_bancario, numero_saques, "Operação falhou! Você não tem saldo suficiente."
    elif valor > limite:
        return saldo, extrato_bancario, numero_saques, "Operação falhou! O valor do saque excede o limite."
    elif numero_saques >= limite_saques:
        return saldo, extrato_bancario, numero_saques, "Operação falhou! Número máximo de saques excedido."
    elif valor <= 0:
        return saldo, extrato_bancario, numero_saques, "Operação falhou! O valor informado é inválido."
    else:
        saldo -= valor
        extrato_bancario += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato_bancario, numero_saques, None  # Retorna None se não houver erro

def extrato(saldo, *, extrato_bancario):  # Renomeado
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_bancario else extrato_bancario)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuarios(nome, data_nascimento, cpf, endereco):
    # Validar se CPF já possui cadastro
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já cadastrado com esse número de CPF!")
            return None  # retornar None se já existir o CPF
        
    # Criar Dicionário para o novo usuário
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)  # Adiciona o novo usuário à lista 
    print("Usuário cadastrado com sucesso!")

# Criar a conta corrente 
def criar_conta(usuario_cpf):
    global numero_conta  # Global para incrementar o número da conta 
    agencia = "0001"

    # Validar se o usuário com o CPF informado já existe
    usuario_localizado = None
    for usuario in usuarios:
        if usuario["cpf"] == usuario_cpf:
            usuario_localizado = usuario
            break

    if not usuario_localizado:
        print("Usuário não localizado!")
        return None  # Retornar None se o usuário não for localizado
     
    # Criar a conta
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_localizado, 
    }

    contas.append(nova_conta)  # Adiciona a nova conta à lista 
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

    numero_conta += 1  # Incrementar o número da conta para a próxima

# Função para listar contas
def listar_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    print("\n================ LISTA DE CONTAS ================")
    for conta in contas:
        usuario_nome = conta["usuario"]["nome"]
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Nome do Usuário: {usuario_nome}")
    print("==================================================")

# Loop principal 
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo, extrato_bancario = depositar(saldo, valor, extrato_bancario)  # Renomeado
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato_bancario, numero_saques, erro = sacar(saldo=saldo, valor=valor, extrato_bancario=extrato_bancario,
                                                             limite=limite, numero_saques=numero_saques,
                                                             limite_saques=LIMITE_SAQUES)
        if erro:
            print(erro)

    elif opcao == "e":
        extrato(saldo, extrato_bancario=extrato_bancario)  # Corrigido

    elif opcao == "c":  # Criar Usuário
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
        cpf = input("Informe o CPF (somente números): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade - estado): ")
        criar_usuarios(nome, data_nascimento, cpf, endereco)

    elif opcao == "cc":  # Criar Conta Corrente
        cpf = input("Informe o CPF do usuário: ")
        criar_conta(cpf)

    elif opcao == "l":  # Listar Contas
        listar_contas()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
