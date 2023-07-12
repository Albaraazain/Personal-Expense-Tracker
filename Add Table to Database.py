import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Az138138138$",
    database="personal_expense_app"
)

cursor = mydb.cursor()

table_sql = """
CREATE TABLE expense (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    amount DECIMAL(10, 2),
    date DATE
)
"""

cursor.execute(table_sql)

mydb.commit()

cursor.close()
mydb.close()

