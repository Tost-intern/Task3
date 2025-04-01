import csv
import os

CSV_FILE = "expenses.csv" 

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount"]) 

print("✅ CSV file initialized with headers.")

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
        print("No expenses found. Add some first.")


def delete_expense():
    date = input("Enter the date (YYYY-MM-DD) or category to delete the expense: ")

    with open(CSV_FILE, mode="r") as file:
        rows = list(csv.reader(file))

    
    rows = [row for row in rows if row[0] != date and row[1] != date]

    
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"✅ Expense with date/category '{date}' deleted.")


def show_expenses_by_category():
    category_expenses = {}

    with open(CSV_FILE, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            category = row[1]
            amount = float(row[2])

            if category not in category_expenses:
                category_expenses[category] = 0
            category_expenses[category] += amount

    print("\nTotal Expenses by Category:")
    print("-" * 30)
    for category, total in category_expenses.items():
        print(f"{category}: ${total}")
    print("-" * 30)


def main():
    while True:
        print("\n📊 Expense Tracker")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Delete Expense")
        print("4️⃣ Show Expenses by Category")
        print("5️⃣ Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            show_expenses_by_category()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
