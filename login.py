import sql

def login():
    cpf = input("CPF: ")
    senha = input("Senha: ")

    conn = sql.conectar()
    cur = conn.cursor()

    cur.execute("SELECT senha, bloqueado, tentativas_login FROM clientes WHERE cpf = ?", (cpf,))
    row = cur.fetchone()

    if not row:
        print("CPF não encontrado")
        conn.close()
        return False

    senha_db, bloqueado, tentativas = row

    if bloqueado:
        print("Conta bloqueada")
        conn.close()
        return False

    if senha == senha_db:
        cur.execute("UPDATE clientes SET tentativas_login = 0 WHERE cpf = ?", (cpf,))
        conn.commit()
        conn.close()
        return cpf   

    tentativas += 1
    if tentativas >= 3:
        cur.execute("UPDATE clientes SET bloqueado = 1, tentativas_login = ? WHERE cpf = ?", (tentativas, cpf))
        print("Conta bloqueada")
    else:
        cur.execute("UPDATE clientes SET tentativas_login = ? WHERE cpf = ?", (tentativas, cpf))
        print("Senha incorreta")

    conn.commit()
    conn.close()
    return False
