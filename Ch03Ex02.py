# user input
personAge = int(input('Enter the age of the individual (in months) to classif them: '))

# if statements for age classifier

if personAge <= 12: # classify as an infant
    print(f'This person at {personAge} months is an infant')
elif 12 < personAge < 156: # classify as a child
    print(f'This person at {personAge} months is a child')
    
elif 156 <= personAge < 240 : # classify as a teenager
     print(f'This person at {personAge} months is a teenager')

elif personAge >= 240 :
     print(f'This person at {personAge} months is an adult')