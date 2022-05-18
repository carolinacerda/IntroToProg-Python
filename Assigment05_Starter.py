# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starting script
# CCerda,5.16.2022,Added code to complete assignment 5
# CCerda,5.17.2022,Improved code for Step 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# Declare variables and constants
objFile = None  # An object that represents a file
strFile = "ToDoList.txt"  # A file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program""")
while True:
    print("-" * 40)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Your Current To Do List Is:")
        for dicRow in lstTable:
            print("  ", dicRow["Task"], "|", dicRow["Priority"])
        print()  # adding a new line for looks
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        print("Type in your task and its priority.")
        strTask = str(input("  Enter a task: ")).strip()
        strPriority = str(input("  Enter a priority [High|Medium|Low]: ")).strip()
        dicRow = {"Task": strTask.title(), "Priority": strPriority.title()}
        lstTable.append(dicRow)
        print()  # adding a new line for looks
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strRemove = input("Which task do you want to remove?: ")
        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():
                lstTable.remove(row)
                print("\n  The task, ", "'", strRemove.title(), "'", ", has been removed.", sep="")
                break
            else:
                pass
        else:
            print("\n  Sorry, the task, ", "'", strRemove.title(), "'", ", doesn't exist in the current To-Do List. "
                                                                      "Please try again.", sep="")
        print()  # adding a new line for looks
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        print("Would you like to save your data?")
        strAnswer = str(input("  Enter 'y' or 'n': "))
        if strAnswer.lower() == "y":
            objFile = open('ToDoList.txt', "w")
            for dicRow in lstTable:
                objFile.write(str(dicRow["Task"]) + ", " + str(dicRow["Priority"]) + "\n")
            objFile.close()
            print("\n  Data saved to file!")
        else:
            print("\n  Data not saved.")
        print()  # adding a new line for looks
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("  Exit complete.")
        break  # and Exit the program

    # Optional - Safety net if no recognized option is inputted by the user.
    else:
        print("  Input not recognized! Please try again.\n")
        continue
