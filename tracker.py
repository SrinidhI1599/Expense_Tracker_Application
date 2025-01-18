# Import the Expense class from the expense module
from expense import Expense

# Define the ExpenseTracker class to manage a collection of expenses
class ExpenseTracker:
    # Constructor method to initialize the ExpenseTracker object
    def __init__(self):
        # Initialize an empty list to store expense objects
        self.expenses = []
    
    # Method to add a new expense to the tracker
    def add_expense(self, description, amount, date):
        # Create a new Expense object using the provided description, amount, and date
        expense = Expense(description, amount, date)
        # Append the newly created expense to the list of expenses
        self.expenses.append(expense)
        # Notify the user that the expense was added successfully
        print("Expense added successfully.")
    
    # Method to display all expenses in the tracker
    def display_expenses(self):
        # Check if there are no expenses in the list
        if not self.expenses:
            # Notify the user that there are no expenses to display
            print("No expenses to display.")
        else:
            # Print a header for the expense list
            print("\nAll Expenses:")
            # Iterate through the list of expenses and print each one
            for expense in self.expenses:
                print(expense)

    # Method to calculate and display the total of all expenses
    def summarize_expenses(self):
        # Use a generator expression to sum the 'amount' attribute of all expense objects
        total = sum(exp.amount for exp in self.expenses)
         # Print the total amount of all expenses, formatted to 2 decimal places
        print(f"\nTotal Expenses: ${total:.2f}")