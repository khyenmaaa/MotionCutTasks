import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """
        Load expenses from the JSON file.
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_expenses(self):
        """
        Save expenses to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description=""):
        """
        Add a new expense to the tracker.
        """
        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        """
        Display all expenses.
        """
        if not self.expenses:
            print("No expenses recorded.")
            return

        for expense in self.expenses:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def category_summary(self):
        """
        Display a summary of expenses by category.
        """
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            amount = expense['amount']
            summary[category] = summary.get(category, 0) + amount

        for category, total in summary.items():
            print(f"Category: {category}, Total: {total}")

    def monthly_summary(self):
        """
        Display a summary of expenses by month.
        """
        summary = {}
        for expense in self.expenses:
            month = expense['date'][:7]
            amount = expense['amount']
            summary[month] = summary.get(month, 0) + amount

        for month, total in summary.items():
            print(f"Month: {month}, Total: {total}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Monthly Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description (optional): ")
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.category_summary()
        elif choice == '4':
            tracker.monthly_summary()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

main()
