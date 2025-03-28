import csv
import os
from collections import defaultdict

CSV_FILE = "expenses.csv"

# Check if the CSV file exists; if not, create it and write the header
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    """Add a new expense to the CSV file."""
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
    amount = input("Enter the amount spent: ")

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense added successfully!\n")

def view_expenses():
    """View all expenses recorded in the CSV file."""
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            print("\n📌 Your Expenses:")
            print("-" * 30)
            for row in expenses:
                print(f"{row[0]} | {row[1]} | ${row[2]}")
            print("-" * 30)

    except FileNotFoundError:
        print("No expenses found. Add some first!")

def delete_expense():
    """Delete an expense by date or category."""
    date = input("Enter the date (YYYY-MM-DD) of the expense to delete (or leave blank to skip): ")
    category = input("Enter the category of the expense to delete (or leave blank to skip): ")

    expenses = []
    deleted = False

    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Read header
        expenses = list(reader)

    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write header back

        for row in expenses:
            if (date and row[0] == date) or (category and row[1] == category):
                deleted = True
                print(f"Deleted expense: {row[0]} | {row[1]} | ${row[2]}")
            else:
                writer.writerow(row)

    if not deleted:
        print("No matching expenses found.")

def show_total_expenses_by_category():
    """Show total expenses summarized by category."""
    category_totals = defaultdict(float)

    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                category = row[1]
                amount = float(row[2])
                category_totals[category] += amount

        print("\n📊 Total Expenses by Category:")
        print("-" * 30)
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")
        print("-" * 30)

    except FileNotFoundError:
        print("No expenses found. Add some first!")

def main():
    """Main function to run the Expense Tracker."""
    while True:
        print("\num Expense Tracker")
        print("1 Add Expense")
        print("2 View Expenses")
        print("3 Delete Expense")
        print("3 Show Total Expenses by Category")
        print("5 Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_total_expenses_by_category()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()