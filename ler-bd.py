import mysql.connector

conexao = mysql.connector.connect(
    host='bcolunajavatest.mysql.uhserver.com',
    user='bcolunajavatest',
    password='@Jvln2019@',
    database='bcolunajavatest',
)

cursor = conexao.cursor()

comando = f'SELECT * FROM insumos'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados

print(resultado)

cursor.close()
conexao.close()