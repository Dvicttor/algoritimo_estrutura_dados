import mysql.connector
from mysql.connector import Error

def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            database="escola",   # nome do banco
            user="root",         # usuário do MySQL
            password="aluno",     # senha do MySQL
            port=3306            # porta padrão do MySQL
        )
        if conexao.is_connected():
            print("Conexão estabelecida com MySQL!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
