# Define the Expense class to represent an individual expense item
class Expense:

    # Constructor method to initialize the properties of the Expense object
    def __init__(self, description, amount, date):

        # 'description' stores the name or purpose of the expense (e.g., "Groceries")
        self.description = description

        # 'amount' stores the monetary value of the expense as a float (e.g., 50.75)
        self.amount = amount

        # 'date' stores the date when the expense was incurred in a string format (e.g., "2025-01-18")
        self.date = date

    # Define a method to return a string representation of the Expense object
    def __str__(self):
        # Returns a formatted string displaying the expense's date, description, and amount
        return f"{self.date}: {self.description} - ${self.amount:.2f}"