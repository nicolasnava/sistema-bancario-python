import sql

def inicializar_banco():
    conn = sql.conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        cpf TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        rg TEXT NOT NULL,
        telefone TEXT NOT NULL,
        cep TEXT NOT NULL,
        rua TEXT NOT NULL,
        numero TEXT NOT NULL,
        bairro TEXT NOT NULL,
        cidade TEXT NOT NULL,
        estado TEXT NOT NULL,
        renda_mensal REAL NOT NULL,
        senha TEXT NOT NULL,
        bloqueado INTEGER DEFAULT 0,
        tentativas_login INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_cliente TEXT NOT NULL,
        tipo TEXT NOT NULL,
        saldo REAL NOT NULL,
        limite_cheque_especial REAL DEFAULT 0,
        ativa INTEGER DEFAULT 1
    )
    """)

    conn.commit()
    conn.close()

