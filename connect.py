import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='SeuUser',
    password='SuaSenha',
    database='pystudy'
)
cursor = connection.cursor()
connection = connection
connection.commit()
connection.commit()