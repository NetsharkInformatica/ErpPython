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

for line in myresult:
   print('line:', line)

#deletar
    