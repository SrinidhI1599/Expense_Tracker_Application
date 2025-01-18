# Expense Tracker

The **Expense Tracker** application helps users manage and track their expenses. It allows users to add, view, and summarize expenses via a command-line interface and a simple web-based interface.

---

## Features

- **Add Expenses**: Users can record expenses with a description, amount, and date.
- **View Expenses**: Displays a list of all recorded expenses.
- **Summarize Expenses**: Calculates and displays the total amount of all expenses.
- **User-Friendly Web Interface**: A simple HTML/JavaScript-based interface for managing expenses.

---

## Project Structure

### Backend Files
1. **`expense.py`**  
   - Defines the `Expense` class to represent individual expenses.
   - Each expense has a `description`, `amount`, and `date`.

2. **`tracker.py`**  
   - Implements the `ExpenseTracker` class to manage a collection of expenses.
   - Provides methods to add expenses, display all expenses, and calculate the total.

3. **`main.py`**  
   - Entry point for the application.
   - Provides a command-line interface to interact with the Expense Tracker.

### Frontend File
1. **`front-end.html`**  
   - Implements a simple user interface using HTML, CSS, and JavaScript.
   - Allows users to add expenses, view all expenses, and see the total expenses dynamically.

---

## How to Run

### Prerequisites
1. **Python 3.7+** installed.
2. Any modern web browser (e.g., Chrome, Firefox, Edge).

---

### Running the Backend
1. Open a terminal and navigate to the project directory.
2. Run the following command to start the command-line interface:
   ```bash
   python main.py


### Example Usage
Expense Tracker Menu
1. Add a new expense
2. View all expenses
3. View total expenses
4. Exit

Enter your choice (1-4): 1
Enter description: Groceries
Enter amount: 50.75
Enter date (YYYY-MM-DD): 2025-01-15
Expense added successfully.

Expense Tracker Menu
1. Add a new expense
2. View all expenses
3. View total expenses
4. Exit

Enter your choice (1-4): 2

All Expenses:
2025-01-15: Groceries - $50.75

Expense Tracker Menu
1. Add a new expense
2. View all expenses
3. View total expenses
4. Exit

Enter your choice (1-4): 3

Total Expenses: $50.75
