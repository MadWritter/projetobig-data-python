import os
from time import sleep
import mysql.connector
from dotenv import load_dotenv

from src.processar_dados_faturamento import processar_dados_faturamento
from src.processar_dados_mais_vendidos import processar_dados_mais_vendidos

# Carregar variáveis do .env
load_dotenv()

# Assinar os valores nas variáveis
MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DATABASE", "banco_pandas")

# Função de conexão com retry no DB do container
def connect_mysql(retries=10, delay=5): # até 10 tentativas, 5 segundos entre elas
    for i in range(retries):
        try:
            conn = mysql.connector.connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DB
            )
            print("Conexão MySQL estabelecida!") # Conectou com o banco
            return conn
        except mysql.connector.Error as e:
            print(f"Erro de conexão ({i+1}/{retries}): {e}") # Erro de conexão, mais uma tentativa
            sleep(delay) # 5 segundos...
    raise Exception("Não foi possível conectar ao MySQL após várias tentativas.") # Somente se as 10 tentativas falharem

conn = connect_mysql()

# Processar os dados
processar_dados_faturamento(conn)
processar_dados_mais_vendidos(conn)

conn.close() # Encerra a conexão com o banco
