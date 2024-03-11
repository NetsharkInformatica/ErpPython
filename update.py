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

#insert
print('inserir cliente?')
sql="Update Cliente  set nome='Joao Jose' where IdCliente ='7'"
mycursor.execute(sql)
mydb.commit()

print('-x-' * 30)
for line in myresult:
   print('line:', line)
print(mycursor.rowcount,'registros inseridos')