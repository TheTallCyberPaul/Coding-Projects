totalBugs = 0

for numberDays in range(1,8):
      dayBugs = int(input(f"Enter the number of bugs collected on day {numberDays}: "))
      totalBugs += dayBugs 
 
if numberDays == 7:
      print(f"You collected a total of {totalBugs} bugs") 