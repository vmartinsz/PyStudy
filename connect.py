import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='47541050',
    database='pystudy'
)
cursor = connection.cursor()
connection = connection
connection.commit()
connection.commit()