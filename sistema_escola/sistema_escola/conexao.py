import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aluno",
            database="escola",  # nome do banco
            port=3306
        )
        if conexao.is_connected():
            print("Conexão estabelecida com MySQL!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None