def calculate_savings(income, expenses):
    #Calculate Savings
    savings = income - expenses
    return f"Total savings: ${savings:.2f}"

def simple_interest(principal, rate, time):
    #Calculate Simple Interest
    si = principal * (rate/100) * time
    total_si = si + principal
    return total_si

def compound_interest(principal, rate, times_compounded, years):
    #Calculate Compound Interest
    ci = principal * (1 + (rate/100) / times_compounded) ** (times_compounded * years)
    total_ci = ci + principal
    return total_ci

def calculate_expenses(expenses):
    sum_total = sum(expenses)
    return sum_total


command = input("Which command would you like to run? Options: savings, simple, compound: ")

if command == "savings":
    income = float(input("What is your income? "))
    num_expenses = int(input("How many expenses do you have? "))
    expenses = []
    for i in range(num_expenses):
        expense = float(input(f"Enter expense {i+1}: "))
        expenses.append(expense)
        total_expenses = calculate_expenses(expenses)
    print(f"Total savings: ${calculate_savings(income, total_expenses)}")
elif command == "simple":
    principal = float(input("What is the principal amount? "))
    rate = float(input("What is the interest rate (in%)? "))
    time = float(input("For how many years? "))
    print(f"Total amount: ${simple_interest(principal, rate, time):.2f}")
elif command == "compound":
    principal = float(input("What is the principal amount? "))
    rate = float(input("What is the interest rate (in%)? "))
    times_compounded = int(input("How many times is the interest compounded per year? "))
    years = int(input("For how many years? "))
    print(f"Total amount: ${compound_interest(principal, rate, times_compounded, years):.2f}")
else:
    print("Invalid Command")

