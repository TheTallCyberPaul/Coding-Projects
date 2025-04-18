years = 0
total_rainfall = 0

print("Enter the number of rainfall years to record: ")  
years = int(input())

for years in range(1,2):
    print("**************")
    print(f"*** Year {years} ***")
    print("**************")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for (year {years}/month {month}): "))
        total_rainfall += rainfall
    for years in range(2,3):
        print("\n**************")
        print(f"*** Year {years} ***")
        print("**************")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for (year {years}/month {month}): "))
        total_rainfall += rainfall
        

months = years * 12
average_rainfall = total_rainfall / months

print(f"\nFor {months} months, there was a total rainfall of {total_rainfall:.1f} inches with and average monthly rainfall of {average_rainfall:.1f} inches.")