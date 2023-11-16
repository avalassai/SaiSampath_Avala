import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Saibaba@123'
)


cursor = dataBase.cursor()


cursor.execute("CREATE DATABASE django_project")


print("DataBase Created Successfully!")