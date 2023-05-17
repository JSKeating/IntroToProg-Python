# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Jordan Keating, 5.15.2023, Added code to options 1-3
# Jordan Keating, 5.16.2023, Added code to options 4-5, completed testing
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt" # Our text file saved on harddrive
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    strData = row.split(",") #split command helps indicate where program should break up the data in each instance.
                            # Without the split, our code will read each full row as one item
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()} #strip removes invisible new line (\n) command from text file
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new task.
    3) Remove an existing task.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Here is your current To Do List: \n")
        for row in lstTable:
            print(row["Task"], " | ", row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        NewTask = input("Please enter your new task: ")
        NewPriority = input("What priority level is this task? (Low, Med, or High): ")
        NewDicRow = {"Task": NewTask, "Priority": NewPriority}
        lstTable.append(NewDicRow)
        while(True):
            another = input("\nYour new task has been saved! Add another? (Y or N): ")
            if another.lower().strip() == "y":
                NewTask = input("Please enter your new task: ")
                NewPriority = input("What priority level is this task? (Low, Med, or High): ")
                NewDicRow = {"Task": NewTask, "Priority": NewPriority}
                lstTable.append(NewDicRow)
            else:
                break
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("As a reminder, here is your current To-Do List:")
        for row in lstTable:
            print(row["Task"])
        itemRemove = input("\nPlease type the name of the task you'd like to remove: ")
        for row in lstTable:
            if row["Task"].lower() == itemRemove.lower():
                lstTable.remove(row)
                print("\n" + itemRemove + " has been removed!")

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        ToDoList = open(strFile, "w")
        for row in lstTable:
            ToDoList.write(row["Task"] + ', ' + row["Priority"] + '\n')
        ToDoList.close()
        print("Data was saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        confirm = input("Press Y to confirm exit or N to return to menu: ")
        if confirm.lower().strip() == "y":
            break  # and Exit the program
        else:
            continue
