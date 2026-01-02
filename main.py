import login
import cadastro
import operacoes
import init_db

init_db.inicializar_banco()


while True:
    print("\n=== BANCO OFICIAL ===")
    print("1 - Login")
    print("2 - Cadastro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cpf_logado = login.login()

        if cpf_logado:
            while True:
                print("\n=== MENU DA CONTA ===")
                print("1 - Depositar")
                print("2 - Sacar")
                print("3 - Transferir")
                print("4 - Ver saldo")
                print("0 - Sair")

                op = input("Escolha: ")

                if op == "1":
                    operacoes.depositar(cpf_logado)
                elif op == "2":
                    operacoes.sacar(cpf_logado)
                elif op == "3":
                    operacoes.transferir(cpf_logado)
                elif op == "4":
                    saldo = operacoes.obter_saldo(cpf_logado)
                    print(f"Saldo atual: R$ {saldo:.2f}")
                elif op == "0":
                    break

    elif opcao == "2":
        cadastro.Cadastro()

    elif opcao == "0":
        print("Encerrando sistema...")
        break
