# Import the ExpenseTracker class from the tracker module
from tracker import ExpenseTracker

# Define the main function that serves as the entry point of the program
def main():
    # Create an instance of the ExpenseTracker class
    tracker = ExpenseTracker()

    # Start an infinite loop for the menu-driven interface
    while True:
        # Print the menu options
        print("\nExpense Tracker Menu")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. View total expenses")
        print("4. Exit")

        # Prompt the user to select an option
        choice = input("Enter your choice (1-4): ")

        # Handle the user's choice
        if choice == '1':  # Add a new expense
            # Prompt the user for expense details
            description = input("Enter description: ")
            try:
                # Prompt for the amount and attempt to convert it to a float
                amount = float(input("Enter amount: "))
            except ValueError:
                # Handle invalid numeric input for the amount
                print("Invalid amount. Please enter a numeric value.")
                continue  # Skip the rest of this iteration and return to the menu
            # Prompt for the date of the expense
            date = input("Enter date (YYYY-MM-DD): ")
            # Call the add_expense method to add the expense to the tracker
            tracker.add_expense(description, amount, date)
        
        elif choice == '2':  # View all expenses
            # Call the display_expenses method to show all expenses
            tracker.display_expenses()
        
        elif choice == '3':  # View total expenses
            # Call the summarize_expenses method to calculate and display the total expenses
            tracker.summarize_expenses()
        
        elif choice == '4':  # Exit the program
            # Print a goodbye message and exit the loop
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        else:  # Handle invalid menu choices
            # Notify the user about the invalid input
            print("Invalid choice. Please try again.")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the program
    main()
