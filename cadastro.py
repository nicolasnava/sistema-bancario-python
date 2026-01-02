import validador
import sql

validador.limpar_tela()

def Cadastro():
    print("=" * 40)
    print("=== Cadastro de Novo Cliente ===")
    print("=" * 40)

    nome = input("Digite seu nome completo: ")
    while len(nome) < 10 or " " not in nome:
        print(" Nome inválido. Deve conter nome e sobrenome.")
        nome = input("Digite seu nome completo: ")

    cpf = input("Digite seu CPF (11 números): ")
    while not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido.")
        cpf = input("Digite seu CPF (11 números): ")

    data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    while data_nascimento.count("/") != 2 or len(data_nascimento) != 10:
        print("Data inválida.")
        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")

    if not validador.verificar_maioridade(data_nascimento):
        print(" Você deve ser maior de idade.")
        return

    rg = input("Digite seu RG (9 números): ")
    while not rg.isdigit() or len(rg) != 9:
        print("RG inválido.")
        rg = input("Digite seu RG (9 números): ")

    telefone = input("Digite seu telefone (11 números): ")
    while not telefone.isdigit() or len(telefone) != 11:
        print("Telefone inválido.")
        telefone = input("Digite seu telefone (11 números): ")

    cep = input("Digite seu CEP (8 números): ")
    while not cep.isdigit() or len(cep) != 8:
        print("CEP inválido.")
        cep = input("Digite seu CEP (8 números): ")

    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")

    estado = input("Estado (UF): ")
    while not estado.isalpha() or len(estado) != 2:
        print("Estado inválido.")
        estado = input("Estado (UF): ")

    renda_mensal = float(input("Digite sua renda mensal (R$): "))
    while renda_mensal < 1000:
        print(" Renda mínima: R$1000")
        renda_mensal = float(input("Digite sua renda mensal (R$): "))

    tipo_escolha = input("Tipo de conta (1 - Corrente | 2 - Poupança): ")
    while tipo_escolha not in ["1", "2"]:
        print("Opção inválida.")
        tipo_escolha = input("Tipo de conta (1 - Corrente | 2 - Poupança): ")

    tipo_conta_db = "corrente" if tipo_escolha == "1" else "poupanca"
    limite = 500.0 if tipo_escolha == "1" else 0.0

    deposito_inicial = float(input("Depósito inicial (mín. R$50): "))
    while deposito_inicial <= 50:
        print("Depósito inválido.")
        deposito_inicial = float(input("Depósito inicial (mín. R$50): "))

    senha = input("Crie uma senha (mín. 6 caracteres): ")
    while len(senha) < 6:
        print("Senha curta.")
        senha = input("Crie uma senha (mín. 6 caracteres): ")

    confirmar = input("Confirme a senha: ")
    while senha != confirmar:
        print("Senhas não coincidem.")
        confirmar = input("Confirme a senha: ")

    conn = sql.conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clientes (
            cpf, nome, data_nascimento, rg, telefone,
            cep, rua, numero, bairro, cidade, estado,
            renda_mensal, senha
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        cpf, nome, data_nascimento, rg, telefone,
        cep, rua, numero, bairro, cidade, estado,
        renda_mensal, senha
    ))

    cursor.execute("""
        INSERT INTO contas (
            cpf_cliente, tipo, saldo, limite_cheque_especial, ativa
        ) VALUES (?, ?, ?, ?, ?)
    """, (
        cpf,
        tipo_conta_db,
        deposito_inicial,
        limite,
        1
    ))

    conn.commit()
    conn.close()

    print("\n" + "=" * 50)
    print("CADASTRO REALIZADO COM SUCESSO!")
    print("=" * 50 + "\n")
