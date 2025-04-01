import csv
import os
from datetime import datetime

CSV_FILE = "expenses.csv"

# Initialize CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"])

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
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
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        if not validate_date(date):
            print("❌ Invalid date format. Please use YYYY-MM-DD.")
            continue
        break
    
    category = input("Enter the category (e.g., Food, Transport): ").strip()
    if not category:
        category = "Uncategorized"
    
    while True:
        amount = input("Enter the amount spent: ").strip()
        if not validate_amount(amount):
            print("❌ Invalid amount. Please enter a positive number.")
            continue
        break

    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, float(amount)])
    
    print("✅ Expense added successfully!\n")

def view_expenses():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header
            expenses = list(reader)

            if not expenses:
                print("No expenses recorded yet.")
                return

            print("\n📌 Your Expenses:")
            print("-" * 50)
            print(f"{'Date':<12} | {'Category':<15} | {'Amount':>10}")
            print("-" * 50)
            for row in expenses:
                print(f"{row[0]:<12} | {row[1]:<15} | ${float(row[2]):>9.2f}")
            print("-" * 50)

    except FileNotFoundError:
        print("No expenses found. Add some first!")
    except Exception as e:
        print(f"Error reading expenses: {e}")

def delete_expense():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            expenses = list(reader)
        
        if len(expenses) <= 1:  # Only header exists
            print("No expenses to delete.")
            return

        print("\nDelete by: 1) Date  2) Category")
        choice = input("Choose an option (1-2): ")
        
        if choice == "1":
            date = input("Enter date to delete (YYYY-MM-DD): ")
            updated_expenses = [row for row in expenses if row[0] != date]
        elif choice == "2":
            category = input("Enter category to delete: ")
            updated_expenses = [row for row in expenses if row[1].lower() != category.lower()]
        else:
            print("❌ Invalid choice.")
            return

        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_expenses)
        
        deleted_count = len(expenses) - len(updated_expenses)
        print(f"✅ Deleted {deleted_count} expense(s) successfully!")

    except Exception as e:
        print(f"Error deleting expenses: {e}")

def total_by_category():
    try:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            expenses = list(reader)
        
        if not expenses:
            print("No expenses recorded yet.")
            return

        categories = {}
        for row in expenses:
            category = row[1]
            amount = float(row[2])
            categories[category] = categories.get(category, 0) + amount

        print("\n📊 Total Expenses by Category:")
        print("-" * 40)
        for category, total in categories.items():
            print(f"{category:<20} | ${total:>9.2f}")
        print("-" * 40)

    except Exception as e:
        print(f"Error calculating totals: {e}")

def main():
    while True:
        print("\n📊 Expense Tracker")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Delete Expense")
        print("4️⃣ Total by Category")
        print("5️⃣ Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_by_category()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()