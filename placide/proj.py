
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict

CSV_FILE = "expenses.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        return amount > 0
    except ValueError:
        return False

def add_expense():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if not validate_date(date):
            print("❌ Invalid date format. Please use YYYY-MM-DD")
            continue
        break
    
    category = input("Enter the category (e.g., Food, Transport): ").capitalize()
    
    while True:
        amount = input("Enter the amount spent: ")
        if not validate_amount(amount):
            print("❌ Invalid amount. Please enter a positive number")
            continue
        break

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            print("\n📌 Your Expenses:")
            print("-" * 50)
            print("Date       | Category  | Amount")
            print("-" * 50)
            for row in expenses:
                print(f"{row[0]} | {row[1]:<9} | ${float(row[2]):,.2f}")
            print("-" * 50)

    except FileNotFoundError:
        print("No expenses found. Add some first!")

def delete_expense():
    print("\n🗑️ Delete Expense")
    print("1. Delete by Date")
    print("2. Delete by Category")
    
    choice = input("Choose an option: ")
    
    if choice not in ['1', '2']:
        print("❌ Invalid choice")
        return
        
    expenses = []
    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    
    if choice == '1':
        date = input("Enter date to delete (YYYY-MM-DD): ")
        expenses = [row for row in expenses if row[0] != date]
    else:
        category = input("Enter category to delete: ").capitalize()
        expenses = [row for row in expenses if row[1] != category]
    
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    
    print("✅ Expenses deleted successfully!")

def show_category_totals():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            totals = defaultdict(float)
            for row in expenses:
                totals[row[1]] += float(row[2])

            print("\n📊 Category Totals:")
            print("-" * 40)
            for category, total in totals.items():
                print(f"{category:<15} | ${total:,.2f}")
            print("-" * 40)

    except FileNotFoundError:
        print("No expenses found. Add some first!")

def plot_expenses():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            totals = defaultdict(float)
            for row in expenses:
                totals[row[1]] += float(row[2])

            categories = list(totals.keys())
            amounts = list(totals.values())

            plt.figure(figsize=(10, 6))
            plt.bar(categories, amounts)
            plt.title('Expenses by Category')
            plt.xlabel('Categories')
            plt.ylabel('Amount ($)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    except FileNotFoundError:
        print("No expenses found. Add some first!")

def main():
    while True:
        print("\n📊 Expense Tracker")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Delete Expense")
        print("4️⃣ Show Category Totals")
        print("5️⃣ Plot Expenses")
        print("6️⃣ Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_category_totals()
        elif choice == "5":
            plot_expenses()
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

    """
    To use this Expense Tracker, you need to install the following modules:
    
    1. matplotlib - For plotting graphs
       pip install matplotlib
    
    2. collections (defaultdict) - This comes built-in with Python, no need to install
    
    How to use the program:
    
    1. Run the program and you'll see a menu with 6 options
    2. Choose an option by entering the corresponding number (1-6):
       - Option 1: Add a new expense (date, category, amount)
       - Option 2: View all your recorded expenses
       - Option 3: Delete a specific expense
       - Option 4: See total expenses by category
       - Option 5: View a bar chart of your expenses by category
       - Option 6: Exit the program
    
    The program stores expenses in a CSV file and allows you to:
    - Track expenses with dates and categories
    - Visualize spending patterns
    - Manage and delete entries
    - View category-wise totals
    
    To start using:
    1. Open terminal/command prompt
    2. Navigate to the program directory
    3. Run: python proj.py
    """
    my
