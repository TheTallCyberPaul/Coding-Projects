# User Input
foodTotal = float(input('Enter the charge for food: ')) # Charge for food

# Math Equations
tipTotal = foodTotal * 0.18 # Get tip total
taxTotal = foodTotal * 0.07 # Get tax total
totalBill = tipTotal + taxTotal + foodTotal # Get total bill amount

# Print Statements 
print(f'The Tip (18%) on the food charge of ${foodTotal:.2f} is ${tipTotal:.2f}') # Prints tip amount
print(f'The tax (7%) on the food charge of ${foodTotal:.2f} is ${taxTotal:.2f}') # Prints tax amount
print(f'The Total amount, including Tax and Tip, is ${totalBill:.2f}')

