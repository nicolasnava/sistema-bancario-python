# 🏦 Sistema Bancário em Python

> 📚 **Projeto Educacional** - Desenvolvido como parte do meu aprendizado em Python e desenvolvimento de software

Sistema de gerenciamento bancário desenvolvido em Python com SQLite, incluindo cadastro de clientes, autenticação e operações financeiras básicas.

## 💡 Sobre Este Projeto

Este é um dos meus **primeiros projetos completos** em Python! Desenvolvi para praticar e consolidar conceitos como:
- Trabalho com banco de dados (SQLite)
- Estruturação de projetos em módulos
- Validações de entrada de dados
- Lógica de negócio
- Persistência de dados

## ✨ Funcionalidades Implementadas

### 👤 Gestão de Clientes
- ✅ Cadastro completo de novos clientes
- ✅ Validação de maioridade (18+ anos)
- ✅ Validação de renda mínima (R$ 1.000,00)
- ✅ Sistema de login com CPF e senha
- ✅ Bloqueio automático após 3 tentativas de login

### 💳 Tipos de Conta
- **Conta Corrente**: Limite de cheque especial de R$ 500,00
- **Conta Poupança**: Sem limite de cheque especial

### 💰 Operações Bancárias
- 📥 **Depósitos**: Adicionar fundos à conta
- 📤 **Saques**: Retirar valores respeitando saldo disponível
- 🔄 **Transferências**: Transferir entre contas via CPF
- 📊 **Consulta de Saldo**: Visualizar saldo atual

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **SQLite3** - Banco de dados relacional
- **datetime** - Manipulação de datas
- **os** - Operações de sistema

## 📦 Estrutura do Projeto

```
sistema-bancario/
│
├── main.py              # Ponto de entrada do sistema
├── cadastro.py          # Módulo de cadastro de clientes
├── login.py             # Módulo de autenticação
├── operacoes.py         # Operações bancárias (depósito, saque, transferência)
├── validador.py         # Funções de validação
├── sql.py               # Configuração do banco de dados
├── init_db.py           # Inicialização das tabelas
└── banco_oficial.db     # Banco de dados SQLite (gerado automaticamente)
```

## 🗄️ Estrutura do Banco de Dados

### Tabela: `clientes`
- cpf (PRIMARY KEY)
- nome, data_nascimento, rg, telefone
- cep, rua, numero, bairro, cidade, estado
- renda_mensal, senha
- bloqueado, tentativas_login

### Tabela: `contas`
- id (AUTOINCREMENT)
- cpf_cliente (FOREIGN KEY)
- tipo (corrente/poupanca)
- saldo, limite_cheque_especial
- ativa (boolean)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/nicolasnava/sistema-bancario-python.git
cd sistema-bancario
```

2. Execute o sistema:
```bash
python main.py
```

O banco de dados será criado automaticamente na primeira execução.

## 📖 Como Usar

### 1️⃣ Primeiro Acesso - Cadastro
```
=== BANCO OFICIAL ===
1 - Login
2 - Cadastro
0 - Sair

Escolha: 2
```

Preencha todos os dados solicitados:
- Nome completo (nome e sobrenome)
- CPF (11 dígitos)
- Data de nascimento (DD/MM/AAAA)
- RG, telefone, endereço completo
- Renda mensal (mínimo R$ 1.000)
- Tipo de conta (Corrente ou Poupança)
- Depósito inicial (mínimo R$ 50)
- Senha (mínimo 6 caracteres)

### 2️⃣ Login e Operações
```
=== BANCO OFICIAL ===
1 - Login

CPF: 12345678900
Senha: ******
```

### 3️⃣ Menu de Operações
```
=== MENU DA CONTA ===
1 - Depositar
2 - Sacar
3 - Transferir
4 - Ver saldo
0 - Sair
```

## 🔒 Validações Implementadas

- ✅ Nome completo (mínimo 10 caracteres, nome e sobrenome)
- ✅ CPF (11 dígitos numéricos)
- ✅ RG (9 dígitos)
- ✅ Telefone (11 dígitos)
- ✅ CEP (8 dígitos)
- ✅ Data de nascimento (formato DD/MM/AAAA)
- ✅ Maioridade (18+ anos)
- ✅ Renda mínima (R$ 1.000)
- ✅ Depósito inicial mínimo (R$ 50)
- ✅ Senha mínima (6 caracteres)
- ✅ Saldo suficiente para saques e transferências

## 📚 O Que Aprendi Desenvolvendo Este Projeto

- Como estruturar um projeto Python em múltiplos módulos
- Trabalhar com banco de dados SQLite
- Criar e gerenciar relacionamentos entre tabelas
- Implementar validações de dados
- Desenvolver lógica de negócio (regras bancárias)
- Controle de fluxo e loops
- Manipulação de datas com datetime
- Tratamento básico de erros

Estou ciente de algumas limitações do projeto e pretendo melhorá-lo futuramente

## 👨‍💻 Autor

**Seu Nome**
- LinkedIn: www.linkedin.com/in/nicolasnava
- GitHub: https://github.com/nicolasnava

---

💬 **Feedback é muito bem-vindo!** Estou em constante aprendizado e adoraria ouvir sugestões de desenvolvedores mais experientes.

⭐ Se este projeto te ajudou de alguma forma ou você tem sugestões, deixe uma estrela e entre em contato!


**Desenvolvido com 💙, Python e muito aprendizado!**