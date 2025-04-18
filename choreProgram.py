# Paul Christiansen
#
# This is a chore sorting program! I made in part for myself and for this assignemt. 
# It was made as I struggle with keeping track of stuff to do so this uses all the 
# fuctions I would want when keeping track of chores!

# Startup list of chores
choreList = ["Take out the trash", "Do the dishes", "Vacuum the floor",
              "Clean the bathroom", "Mow the lawn", "Dusting",
              "Laundry", "Grocery shopping", "Meal Prep", "Water Plants"]  # Initialize a list of chores

# Function to display the startup banner
def displayBanner():
    print("=========================================================")  # Print a separator line
    print("            Paul's Chore Tracker Program!           ")  # Print the welcome message
    print("=========================================================")  # Print a separator line

# 1) Function to display the list of chores
def displayChores():
    print("\n----- Current Chores -----")  # Print a header for the chore list
    if not choreList:  # Check if the chore list is empty
        print("The chore list is currently empty.")  # Print message if the list is empty
    else:
        for index, chore in enumerate(choreList):  # Iterate through the chore list, getting both the index and chore
            print(f"{index + 1}. {chore}")  # Print the chore number (index + 1) and the chore
    print("--------------------------")  # Print a separator line

# 2) Function to add a chore to the end of the list
def addChoreToEnd():
    newChore = input("Enter the chore to add to the end of the list: ")  # Prompt the user to enter a new chore
    choreList.append(newChore)  # Add the new chore to the end of the chore list
    print(f"'{newChore}' has been added to the chore list.")  # Print a confirmation message
    displayChores()  # Display the updated chore list

# 3) Function to insert a chore into the list
def insertChore():
    index = int(input(f"Enter the position (1-{len(choreList) + 1}) to insert the chore: ")) - 1  # Prompt for position, adjust to 0-based index
    newChore = input("Enter the chore to insert: ")  # Prompt the user to enter the chore to insert
    choreList.insert(index, newChore)  # Insert the new chore at the specified index
    print(f"'{newChore}' has been inserted at position {index + 1}.")  # Print confirmation message
    displayChores()  # Display the updated chore list

# 4) Function to remove a chore from the list by value
def removeChoreByValue():
    choreToRemove = input("Enter the chore to remove from the list: ")  # Prompt the user for the chore to remove
    if choreToRemove in choreList:  # Check if the chore is in the list
        choreList.remove(choreToRemove)  # Remove the chore from the list
        print(f"'{choreToRemove}' has been removed from the chore list.")  # Print confirmation
        displayChores()  # Display the updated chore list
    else:
        print(f"'{choreToRemove}' is not in the chore list.")  # Print message if the chore is not found

# 5) Function to remove a chore from the list by index
def removeChoreByIndex(): #renamed function
    if not choreList:  # Check if the chore list is empty
        print("The chore list is empty. There is nothing to remove.")  # Print message if empty
        return  # Return to the calling function
    index = int(input(f"Enter the position (1-{len(choreList)}) of the chore to remove: ")) - 1  # Get index and adjust to be 0-based
    if 0 <= index < len(choreList):  # Check if the index is valid
        removedChore = choreList.pop(index)  # Remove and get the removed chore
        print(f"'{removedChore}' has been removed from position {index + 1}.")  # Print confirmation
        displayChores()  # Display the updated chore list
    else:
        print("Invalid position. Please enter a valid position.")  # Print error message

# 6) Function to sort the chore list
def sortChoreList():
    choreList.sort()  # Sort the chore list in ascending order
    print("The chore list has been sorted in ascending order.")  # Print message
    displayChores()  # Display the sorted chore list

# 7) Function to reverse the chore list
def reverseChoreList():
    choreList.reverse()  # Reverse the order of elements in the chore list
    print("The chore list has been reversed.")  # Print message
    displayChores()  # Display the reversed chore list

# 8) Function to count occurrences of a chore
def countChoreOccurrences():
    choreToCount = input("Enter the chore to count: ")  # Get the chore to count
    count = choreList.count(choreToCount)  # Count occurrences of the chore
    print(f"The chore '{choreToCount}' appears {count} times in the chore list.")  # Print the count

# 9) Function to extend the chore list
def extendChoreList():
    choresToAdd = input("Enter chores to add, separated by commas: ").split(",")  # Get chores, split by commas
    choresToAdd = [chore.strip() for chore in choresToAdd]  # Remove extra spaces from input
    choreList.extend(choresToAdd)  # Add the new chores to the chore list
    print(f"The chores '{', '.join(choresToAdd)}' have been added to the chore list.")  # Print confirmation
    displayChores()  # Display the updated chore list

# 10) Function to clear the chore list
def clearChoreList():
    choreList.clear()  # Remove all items from the chore list
    print("All chores have been removed from the chore list.")  # Print message
    displayChores()  # Display the empty list

# 11) Function to copy the chore list
def copyChoreList():
    newChoreList = choreList.copy()  # Create a copy of the chore list
    print("The chore list has been copied.")  # Print message
    print("Original chore list:")  #message
    displayChores()  # Display the original chore list
    print("Copied chore list:")
    print("\n----- Copied Chore List Items -----")
    if not newChoreList:  # Check if the copied list is empty
        print("The list is currently empty.")  # Print message if empty
    else:
        for index, chore in enumerate(newChoreList):  # Iterate through the copied list
            print(f"{index + 1}. {chore}")  # Display chore number and chore
    print("------------------------------")

# 12) Function to remove and return a chore by index
def popChoreByIndex():
    if not choreList:  # Check if the chore list is empty
        print("The chore list is empty. Cannot remove from an empty list.")  # Print message if empty
        return  # Return to the calling function

    index = int(input(f"Enter the index (1-{len(choreList)}) of the chore to remove and return: ")) - 1 # Get index from user and adjust to be 0-based
    if 0 <= index < len(choreList):  # Check if the index is valid
        poppedChore = choreList.pop(index)  # Remove the chore at the given index and store it
        print(f"Removed chore '{poppedChore}' from index {index + 1}.")  # Print confirmation message
        displayChores()  # Display the updated chore list
    else:
        print("Invalid index.  Please enter a valid index.")  # Print error message

# Function to display the menu
def displayMenu():
    print("\n----- Menu -----")
    print("1.  Display the list of chores")
    print("2.  Add a chore to the end")
    print("3.  Insert a chore at a position")
    print("4.  Remove a chore by value")
    print("5.  Remove a chore by index")
    print("6.  Sort the chore list")
    print("7.  Reverse the chore list")
    print("8.  Count occurrences of a chore")
    print("9.  Extend the chore list")
    print("10. Clear the chore list")
    print("11. Copy the chore list")
    print("12. Remove and return a chore by index") 
    print("13. Exit the program")
    print("------------------")

# Function to exit the program
def exitProgram():
    print("\nThank you for using the Chore Tracker Program!  Hope you get them done!")  # Print exit message

# Main function
def main():
    displayBanner()  # Display the banner
    continueProgram = True  # Initialize the loop control variable

    while continueProgram:  # Main loop to keep the program running
        displayMenu()  # Display the menu
        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == '1':
            displayChores()  # Call function to display chores
        elif choice == '2':
            addChoreToEnd()  # Call function to add chore to the end
        elif choice == '3':
            insertChore()  # Call function to insert
        elif choice == '4':
            removeChoreByValue()  # Call function to remove by value
        elif choice == '5':
            removeChoreByIndex()  # Call the new function
        elif choice == '6':
            sortChoreList()  # Call function to sort
        elif choice == '7':
            reverseChoreList()  # Call function to reverse
        elif choice == '8':
            countChoreOccurrences()  # Call function to count
        elif choice == '9':
            extendChoreList()  # Call function to extend
        elif choice == '10':
            clearChoreList()  # Call function to clear
        elif choice == '11':
            copyChoreList()  # Call function to copy
        elif choice == '12':
            popChoreByIndex()  # Call the new function
        elif choice == '13':
            confirmation = input("Are you sure you want to exit? (yes/no): ")  # Confirm exit
            if confirmation.lower() == "yes":  # If user confirms
                exitProgram()  # Call exit function
                continueProgram = False  # Set to false to exit loop
            else:
                print("Returning to the menu.")  #message
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Call the main function to start the program
