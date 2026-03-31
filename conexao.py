from mysql.connector import Error
import mysql.connector

# Função para conectar ao banco
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            database="escola",   # nome do banco
            user="root",         # usuário do MySQL
            password="aluno",    # senha do MySQL
            port=3306            # porta padrão do MySQL
        )
        if conexao.is_connected():
            print("Conexão estabelecida com MySQL!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Exemplo de uso da conexão
conn = conectar_banco()
if conn is None:
    exit()  # sai se não conseguiu conectar

cursor = conn.cursor()

# Define SQL
sql = "INSERT INTO alunos (nome, data, cpf) VALUES (%s, %s, %s)"

# Defina os valores de exemplo
nome = "João"
data = "2000-01-01"
cpf = "12345678900"

# Loop de inserção
for i in range(10):
    valores = (nome, data, cpf + str(i))
    cursor.execute(sql, valores)

conn.commit()

print("10 registros inseridos!")

cursor.close()
conn.close()