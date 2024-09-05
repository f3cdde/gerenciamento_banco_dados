import psycopg2

# Conectando ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="db"
)

# Criando um cursor para executar comandos SQL
cur = conn.cursor()

# Inserindo um novo cliente
cur.execute("""
    INSERT INTO clientes (nome, email, telefone)
    VALUES (%s, %s, %s)
""", ("João Silva", "joao.silva@example.com", "123456789"))

# Commit das mudanças
conn.commit()

# Selecionando todos os clientes
cur.execute("SELECT * FROM clientes")
clientes = cur.fetchall()

# Exibindo os clientes
for cliente in clientes:
    print(cliente)

# Fechando o cursor e a conexão
cur.close()
conn.close()
