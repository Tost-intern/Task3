import csv
import os
from collections import defaultdict

CSV_FILE = "expenses.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport): ")
    amount = input("Enter the amount spent: ")

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            print("\n📌 Your Expenses:")
            print("-" * 30)
            for i, row in enumerate(expenses, start=1):
                print(f"{i}. {row[0]} | {row[1]} | ${row[2]}")
            print("-" * 30)
    except FileNotFoundError:
        print("No expenses found. Add some first!")

def delete_expense():
    view_expenses()
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        with open(CSV_FILE, mode="r") as file:
            reader = list(csv.reader(file))
        
        if 0 <= index < len(reader) - 1:
            del reader[index + 1]
            with open(CSV_FILE, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(reader)
            print("✅ Expense deleted successfully!\n")
        else:
            print("❌ Invalid selection.")
    except (ValueError, IndexError):
        print("❌ Invalid input. Try again.")

def show_most_expensive():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            most_expensive = max(expenses, key=lambda x: float(x[2]))
            print(f"\n💰 Most Expensive Expense: {most_expensive[0]} | {most_expensive[1]} | ${most_expensive[2]}\n")
    except FileNotFoundError:
        print("No expenses found.")

def show_total_by_category():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            category_totals = defaultdict(float)
            for row in expenses:
                category_totals[row[1]] += float(row[2])

            print("\n📊 Total Expenses by Category:")
            print("-" * 30)
            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")
            print("-" * 30)
    except FileNotFoundError:
        print("No expenses found.")

def main():
    while True:
        print("\n📊 Expense Tracker")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Delete Expense")
        print("4️⃣ Show Most Expensive Expense")
        print("5️⃣ Show Total Expenses by Category")
        print("6️⃣ Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_most_expensive()
        elif choice == "5":
            show_total_by_category()
        elif choice == "6":
            print("👋 See you!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
