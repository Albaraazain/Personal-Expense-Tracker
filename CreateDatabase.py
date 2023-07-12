import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Az138138138$",
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE personal_expense_app")

mydb.commit()

cursor.close()
mydb.close()
