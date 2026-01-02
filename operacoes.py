import sql


def obter_saldo(cpf):
    conn = sql.conectar()
    cur = conn.cursor()

    cur.execute(
        "SELECT saldo FROM contas WHERE cpf_cliente = ? AND ativa = 1",
        (cpf,)
    )
    row = cur.fetchone()
    conn.close()

    if not row:
        print("❌ Conta não encontrada ou inativa.")
        return None

    return row[0]


def depositar(cpf):
    try:
        valor = float(input("Valor depósito: "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    if valor <= 0:
        print("❌ O valor do depósito deve ser maior que zero.")
        return

    saldo = obter_saldo(cpf)
    if saldo is None:
        return

    novo = saldo + valor

    conn = sql.conectar()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contas SET saldo = ? WHERE cpf_cliente = ? AND ativa = 1",
        (novo, cpf)
    )

    cur.execute("""
        INSERT INTO movimentacoes
        (cpf_cliente, tipo, valor, saldo_apos, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (
        cpf, "deposito", valor, novo, "Depósito em conta"
    ))

    conn.commit()
    conn.close()

    print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")


def sacar(cpf):
    saldo = obter_saldo(cpf)
    if saldo is None:
        return

    print(f"Saldo atual: R$ {saldo:.2f}")

    try:
        valor = float(input("Valor saque: "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    if valor <= 0:
        print("❌ O valor do saque deve ser maior que zero.")
        return

    if valor > saldo:
        print("❌ Saldo insuficiente.")
        return

    novo = saldo - valor

    conn = sql.conectar()
    cur = conn.cursor()

    cur.execute(
        "UPDATE contas SET saldo = ? WHERE cpf_cliente = ? AND ativa = 1",
        (novo, cpf)
    )

    cur.execute("""
        INSERT INTO movimentacoes
        (cpf_cliente, tipo, valor, saldo_apos, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (
        cpf, "saque", valor, novo, "Saque em conta"
    ))

    conn.commit()
    conn.close()

    print("✅ Saque realizado com sucesso.")


def transferir(origem):
    destino = input("CPF destino: ")

    if not destino.isdigit() or len(destino) != 11:
        print("❌ CPF destino inválido.")
        return

    try:
        valor = float(input("Valor da transferência: "))
    except ValueError:
        print("❌ Valor inválido.")
        return

    if valor <= 0:
        print("❌ O valor deve ser maior que zero.")
        return

    saldo_origem = obter_saldo(origem)
    if saldo_origem is None:
        return

    if valor > saldo_origem:
        print("❌ Saldo insuficiente.")
        return

    conn = sql.conectar()
    cur = conn.cursor()


    cur.execute(
        "SELECT saldo FROM contas WHERE cpf_cliente = ? AND ativa = 1",
        (destino,)
    )
    row_destino = cur.fetchone()

    if not row_destino:
        print("❌ Conta destino não encontrada.")
        conn.close()
        return

    novo_saldo_origem = saldo_origem - valor
    novo_saldo_destino = row_destino[0] + valor


    cur.execute(
        "UPDATE contas SET saldo = ? WHERE cpf_cliente = ?",
        (novo_saldo_origem, origem)
    )


    cur.execute(
        "UPDATE contas SET saldo = ? WHERE cpf_cliente = ?",
        (novo_saldo_destino, destino)
    )


    cur.execute("""
        INSERT INTO movimentacoes
        (cpf_cliente, tipo, valor, saldo_apos, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (
        origem, "transferencia", valor, novo_saldo_origem,
        f"Transferência para {destino}"
    ))

    cur.execute("""
        INSERT INTO movimentacoes
        (cpf_cliente, tipo, valor, saldo_apos, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (
        destino, "transferencia", valor, novo_saldo_destino,
        f"Transferência de {origem}"
    ))

    conn.commit()
    conn.close()

    print("✅ Transferência realizada com sucesso.")
