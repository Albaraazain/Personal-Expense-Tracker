from flask import Flask, render_template, request, redirect
import mysql.connector

# Create the Flask app object, __name__ is a special variable in Python that is set to the name of the module in which it is used
app = Flask(__name__)

# Create the route for the home page
@app.route('/')
def home():
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enter your password here",
        database="personal_expense_app"
    )

    # Create the cursor to execute SQL queries and fetch data from the database
    cursor = mydb.cursor()
    # The concept of the cursor is similar to the concept of the file handler in Python

    # Execute SQL query to fetch expenses
    # Select all columns from the expense table
    cursor.execute("SELECT * FROM expense")
    # Fetch all the rows returned by the query
    expenses = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    mydb.close()

    # Render the home page with the expenses
    return render_template('expenses.html', expenses=expenses)

# Create the route for the add expense page
# here the method is POST because we are sending data to the server, not fetching data from the server
# here when the user submits the form, it will route to the add_expense route and execute the code in the add_expense function
@app.route('/add_expense', methods=['POST'])
def add_expense():
    # Get the expense details from the form
    # request is a global variable that contains the data sent from the client
    description = request.form['description'] # request.form is a dictionary that contains the data sent from the form, the keys are the names of the form fields
    amount = float(request.form['amount'])
    date = request.form['date']

    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enter your password here",
        database="personal_expense_app"
    )
    cursor = mydb.cursor()

    # Execute SQL query to insert the new expense
    sql = "INSERT INTO expense (description, amount, date) VALUES (%s, %s, %s)"
    values = (description, amount, date)
    cursor.execute(sql, values)

    # Commit the changes and close the cursor and database connection
    mydb.commit()
    cursor.close()
    mydb.close()

    return redirect('/')

@app.route('/delete_expense/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Enter your password here",
        database="personal_expense_app"
    )
    cursor = mydb.cursor()

    # Execute SQL query to delete the expense with the given ID
    sql = "DELETE FROM expense WHERE id = %s"
    value = (expense_id,)
    cursor.execute(sql, value)

    # Commit the changes and close the cursor and database connection
    mydb.commit()
    cursor.close()
    mydb.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
