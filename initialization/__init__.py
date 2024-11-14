import sqlite3

connect = sqlite3.connect("./data/clientes.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido TEXT NOT NULL,
    formaDePagamento TEXT NOT NULL,
    valorDaConta REAL NOT NULL
 )
 ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pizzas (
    sabor TEXT PRIMARY KEY,
    tempoDePreparo TEXT NOT NULL,
    preco REAL NOT NULL,
    tamanhoDaPizza TEXT NOT NULL,
    tipoDaPizza TEXT NOT NULL
 )
 ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Funcionarios (
    numeroDeContrato INTEGER PRIMARY KEY AUTOINCREMENT,
    idade INTEGER NOT NULL,
    nome TEXT NOT NULL,
    numero TEXT NOT NULL,
    especializacao TEXT NOT NULL
 )
 ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pizzarias (
    cnpj TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    bairro TEXT NOT NULL,
    rua TEXT NOT NULL,
    numero INTEGER NOT NULL
 )
 ''')