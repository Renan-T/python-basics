def ask_name():
    name = input("What is your name? ").capitalize()
    return name

def calculate_expenses(expenses):
    sum_total = sum(expenses)
    return sum_total

exp = [20.3, 50.3, 70.1, 86.3]

command = input("Which command would you like to run? Options: expenses, ask_name: ")

if command == 'expenses':
    print(calculate_expenses(exp))
elif command == 'ask_name':
    print(ask_name())
else:
    print("invalid command")