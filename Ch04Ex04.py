count = 0
total = 0
minimum = None
maximum = None
finished = False  # Flag to control the loop

while not finished:  # Loop until finished is set to True
    count += 1
    try:
        num = float(input(f"Enter a positive number to add and negative number to quit - Number {count:02}: "))

        if num <= 0:
            finished = True  # Set flag to true to end the loop
        else:  # Only process if a positive number was entered
            total += num

            if minimum is None or num < minimum:
                minimum = num
            if maximum is None or num > maximum:
                maximum = num

    except ValueError:
        print("Invalid input. Please enter a number.")
        count -= 1  # Decrement count as the number was invalid

if count == 1 and total == 0:  # Check if no positive numbers were entered
    print("No positive numbers were entered.")


average = total / (count - 1)
print("")
print(f"The minimum of all {count - 1} numbers is {minimum}")
print(f"The maximum of all {count - 1} numbers is {maximum}")
print(f"The average of all {count - 1} numbers is {average:.1f}")
print(f"The total of all {count - 1} numbers is {total}")
