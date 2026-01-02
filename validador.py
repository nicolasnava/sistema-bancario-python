from datetime import datetime

def verificar_maioridade(data_nascimento):
    formato = "%d/%m/%Y"
    data_nascimento = datetime.strptime(data_nascimento, formato)
    data_atual = datetime.now()
    idade = data_atual.year - data_nascimento.year
    if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    if idade >= 18:
        return True
    else:
        return False

def limpar_tela():
    import os
    os.system('cls')

def validar_renda(renda):
    if renda <1000:
        print("Renda insuficiente para abertura de conta.")
        return False
    return True