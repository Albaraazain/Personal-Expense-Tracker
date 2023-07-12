import unittest
from flask import Flask
import app  # replace with the name of your Flask app script


class YourFlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()
        self.client.testing = True

    def test_add_expense(self):
        response = self.client.post('/add_expense', data={
            'date': '2023-07-10',
            'amount': '100.00',
            'description': 'Test expense'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Expense added successfully!')


if __name__ == '__main__':
    unittest.main()
