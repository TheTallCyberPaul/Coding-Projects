years = int(input("Enter the number of rainfall years to record: "))
total_rainfall = 0
months = years * 12

for year in range(1, years + 1):
    print(f"\n**\n Year {year} \n**")
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for (year {year}/month {month}): "))
        total_rainfall += rainfall

average_rainfall = total_rainfall / months

print(f"For {months} months, there was a total rainfall of {total_rainfall} inches with and average monthly rainfall of {average_rainfall:.1f} inches.")