import mysql.connector

mydb= mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='m4th3u5ct42',
    database='python'
    
)
mycursor=mydb.cursor()
##consulta Tabela
mycursor.execute('SELECT * FROM Cliente')
myresult=mycursor.fetchall()


#deletar
print('deletar cliente?')
sql="DELETE FROM Cliente WHERE IdCliente='3'"
mycursor.execute(sql)
mydb.commit()

print('-x-' * 30)

print(mycursor.rowcount,'registros deletados')