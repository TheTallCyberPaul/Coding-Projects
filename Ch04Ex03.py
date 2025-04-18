# Salary Calculation Program

# User input
days = int(input("Enter the number of days: \n"))

total_pennies = 0
daily_salary = 1  # Start with one penny
print("Day:\tPennies\t\tBalance")
print("--------------------------------------------")
    
for day in range(1, days + 1):
    total_pennies += daily_salary
    print(f"{day}         ${daily_salary / 100:,.2f}      ${total_pennies / 100:,.2f}      ")
    daily_salary *= 2  # Double the salary for the next day
    
total_salary = total_pennies / 100
print("--------------------------------------------")
print(f"The total salary for {days} days is: ${total_salary:,.2f}")

