import csv
from collections import defaultdict

CSV_FILE = 'expenses.csv'

def add_expense():
    date = input('Enter date (YYYY-MM-DD): ')
    category = input('Enter category (Food, Travel, etc): ')
    description = input('Enter description: ')
    amount = float(input('Enter amount: '))

    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print('Expense added successfully!')

def read_expenses():
    expenses = []
    try:
        with open(CSV_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])
                expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

def monthly_summary():
    expenses = read_expenses()
    summary = defaultdict(float)

    for e in expenses:
        month = e['date'][:7]
        summary[month] += e['amount']

    print('\nMonthly Summary:')
    for month, total in summary.items():
        print(f'{month}: ₹{total:.2f}')

def category_summary():
    expenses = read_expenses()
    summary = defaultdict(float)

    for e in expenses:
        summary[e['category']] += e['amount']

    print('\nCategory Summary:')
    for cat, total in summary.items():
        print(f'{cat}: ₹{total:.2f}')

def highest_lowest_expense():
    expenses = read_expenses()
    if not expenses:
        print('No expenses found.')
        return

    highest = max(expenses, key=lambda x: x['amount'])
    lowest = min(expenses, key=lambda x: x['amount'])

    print('\nHighest Expense:', highest)
    print('Lowest Expense:', lowest)

def menu():
    while True:
        print('\n--- Personal Expense Tracker ---')
        print('1. Add Expense')
        print('2. Monthly Summary')
        print('3. Category Summary')
        print('4. Highest & Lowest Expense')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_expense()
        elif choice == '2':
            monthly_summary()
        elif choice == '3':
            category_summary()
        elif choice == '4':
            highest_lowest_expense()
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    menu()
