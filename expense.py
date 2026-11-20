import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    category = input("Category (e.g., Food, Transport, Bills): ").strip()
    description = input("Description: ").strip()
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expenses.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "category": category,
        "description": description,
        "amount": amount
    })
    save_expenses(expenses)
    print("Expense saved.")

def view_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    by_category = {}
    print("\n--- All Expenses ---")
    for idx, item in enumerate(expenses, 1):
        print(f"{idx}. [{item['date']}] {item['category']} - {item['description']}: {item['amount']:.2f}")
        total += item["amount"]
        by_category[item["category"]] = by_category.get(item["category"], 0) + item["amount"]

    print("\n--- Spending by Category ---")
    for cat, cat_total in by_category.items():
        print(f"{cat}: {cat_total:.2f}")
    print(f"Total Spent: {total:.2f}\n")

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense | 2. View Summary | 3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
