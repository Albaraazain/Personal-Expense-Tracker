
# Expense Tracker

Expense Tracker is a web application that allows you to keep track of your expenses. It provides a simple interface to add, view, and delete expenses, helping you manage your financial records effectively.

## Features

- Add new expenses by providing a description, amount, and date.
- View a list of all expenses with their corresponding details.
- Delete expenses individually as needed.
- Convenient "Today" and "Yesterday" buttons to easily set the date for adding an expense.

## Technologies Used

- HTML (HyperText Markup Language): Provides the structure and content of the webpages.
- CSS (Cascading Style Sheets): Adds styles, layouts, and design elements to the HTML elements.
- JavaScript: Adds interactivity and dynamic behavior to the webpages.
- Python: The programming language used for the backend server-side logic.
- Flask (a micro web framework for Python): Handles routing, request handling, and template rendering on the server-side.
- Jinja (a template engine for Python): Integrates with Flask to dynamically render HTML templates.
- MySQL (a relational database management system): Stores and retrieves expense data in a structured manner.

## Getting Started

To get started with the Expense Tracker application, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/Albaraazain/Personal-Expense-Tracker.git
   ```

2. Install the required dependencies. Assuming you have Python and pip installed, navigate to the project directory and run:
   ```
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Install and configure MySQL on your machine or use an existing MySQL server.
   - Create a new MySQL database for the Expense Tracker application.
   - Update the `app.py` file with your MySQL database connection details. Look for the section where the database connection is established and modify the `host`, `user`, `password`, and `database` variables accordingly.

4. Start the application by running the following command:
   ```
   python app.py
   ```

5. Open your web browser and visit `http://localhost:5000` to access the Expense Tracker.

## Usage

1. Add Expense:
   - Enter the expense description, amount, and date in the provided form.
   - Click the "Add Expense" button to add the expense to the list.

2. View Expenses:
   - The list of expenses will be displayed in a table format.
   - Each expense will have a description, amount, and date.
   - To delete an expense, click the "Delete" button next to the corresponding expense.

3. Date Buttons:
   - Use the "Today" button to set the date field to the current date.
   - Use the "Yesterday" button to set the date field to the previous day.

## Further Explanations


- ### JavaScript:

  - **Importance:** JavaScript plays a crucial role in adding interactivity and dynamic behavior to the Expense Tracker web application. It runs on the client-side, allowing for real-time interactions without requiring page reloads.
   
  - **Purpose:** In this project, JavaScript is responsible for handling the date buttons ("Today" and "Yesterday") functionality. When a user clicks on these buttons, JavaScript retrieves the current or previous date and updates the date input field accordingly. This feature provides convenience and saves users from manually entering the date.
  
- ### Flask

  - **Importance:** Flask is the backend web framework that handles the server-side logic of your Expense Tracker application. It manages the routing, request handling, and template rendering, allowing for the dynamic generation of webpages.
  
  - **Purpose:** In this project, Flask enables the following functionalities:
  Routing: Flask defines routes for different endpoints (e.g., adding expenses, deleting expenses) and maps them to corresponding Python functions.
  Form Submission: Flask handles the submission of the expense form by receiving the data sent from the frontend, validating it, and storing it in the MySQL database.
  Template Rendering: Flask integrates with Jinja, a templating engine, to dynamically render HTML templates with data retrieved from the MySQL database. This allows the display of expense details and the generation of the expenses table.
  
- ### MySQL:

  - **Importance:** MySQL serves as the database management system for your Expense Tracker application. It provides a reliable and efficient storage solution for organizing and retrieving expense data.
  
  - **Purpose:** In this project, MySQL fulfills the following tasks:
  Data Storage: MySQL stores the expense records in a structured manner, allowing for efficient querying, retrieval, and manipulation of expense data.
  Data Retrieval: Flask interacts with the MySQL database to fetch the expense data and pass it to the frontend for rendering in the expenses table.
  Data Deletion: When a user clicks the "Delete" button for a specific expense, Flask sends a request to MySQL to remove the corresponding record from the database.


## Contributing

Contributions to the Expense Tracker project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
