import mysql.connector

# conexão com banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aluno",
    database="faculdade"
)

cursor = conn.cursor()

# cria tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    data_nascimento VARCHAR(10),
    cpf VARCHAR(14)
)
""")

nome = input("Nome: ")
data = input("Data nascimento: ")
cpf = input("CPF: ")

sql = "INSERT INTO alunos (nome, data_nascimento, cpf) VALUES (%s,%s,%s)"

# repetição 10 vezes
for i in range(10):
    valores = (nome, data, cpf + str(i))
    cursor.execute(sql, valores)

conn.commit()

print("10 registros inseridos!")

cursor.close()
conn.close()

