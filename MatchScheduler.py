# Generates placeholder values and schedules for a tournament match

import math

# Checks if input is integer
def isInteger(value):
    try:
        number = int(value)
        return True
    except ValueError:
        return False

# Gets and verifies number inputted by user
def numericInput(prompt, minValue = 1):
    value = input(prompt)
    while(isInteger(value) is not True or int(value) < minValue):
        value = input("Invalid input, please try again: ")
    return value

# Checks if user input is valid from a list of options
def validateUserInput(options: list, value: str):
    # Returns true if item is in list regardless of case
    if any(item.lower() == value.lower() for item in options):
        return True
    # Returns true if input matches first character of options
    elif any(item.lower().startswith(value.lower()) for item in options):
        return True
    return False

# Prints out values similar to a comma separated values (CSV) format
def printGroups(values: list):
    # Gets the group with the largest number of competitors
    maxGroupSize = len(max(values, key=len))
    # Stores string output
    output = []

    for i in range(maxGroupSize):
        row = ""
        for j in values:
            # If index does not exist, add comma
            if (len(j) - 1 < i):
                row += ","
            # Else add placeholder
            else:
                row += j[i] + ","
        # Add row to output list
        output.append(row[:-1])
    
    # Print items in list
    print("Group composition (CSV format): ")
    for i in output:
        print(i)

# Main function
def main():
    # Asks user to input number of competitors and groups to be drawn
    competitors = numericInput("Enter the number of competitors (minimum 3): ", minValue=3)
    groups = numericInput("Enter the number of groups (minimum 1): ")

    # If any group has less than 3 competitors, ask user to re-enter input
    while (int(competitors) / int(groups) < 3):
        print("Inputs are invalid; each group must have at least 3 competitors")
        competitors = numericInput("Enter the number of competitors: ")
        groups = numericInput("Enter the number of groups: ")

    # Default values of group position input is "S" for "smaller groups first"
    groupPositions = "S"
    # Default value of group label input is "N" for "label groups by numbers"
    groupLabel = "N"

    # Gets the minimum number of competitors each group will have
    minCompetitorsPerGroup = math.floor(int(competitors)/int(groups))

    # Checks if at least one group has an uneven number of competitors
    if(int(competitors) % int(groups) != 0):
        # Asks user whether to place larger groups at the beginning or end of the group stack
        print("An uneven number of groups will be created. Please select whether to start with the largest or smallest groups.")
        print("L or Largest: begin with larger groups")
        print("S or Smallest: begin with smaller groups")
        # Gets user input
        groupPositions = input()
        # Asks for user input again if input is invalid
        while(validateUserInput(["Largest", "Smallest"], groupPositions) is False):
            groupPositions = input("Input is invalid, please try again. Valid input is '(L)argest' or '(S)mallest'")

    # Checks if there are less than 27 groups
    if(int(groups) < 27):
        # Asks user to label groups by letters or numbers
        print("Please select whether to identify groups by letters or numbers")
        print("L or Letters: use letters (e.g., A1, A2)")
        print("N or Numbers: use numbers (e.g., 1-1, 1-2)")
        # Gets user input
        groupLabel = input()
        # Asks for user input again if input is invalid
        while(validateUserInput(["Letters", "Numbers"], groupLabel) is False):
            groupLabel = input("Input is invalid, please try again. Valid input is '(L)etters' or '(N)umbers'")

    # Stores groups created
    groupOutput = []
    
    # True if user input is "s" or "smallest"
    smallerGroupsFirst = (groupPositions.lower() == "smallest" or groupPositions.lower() == "s")
    # True if user input is "n" or "number"
    labelGroupsByNumber = (groupLabel.lower() == "number" or groupLabel.lower() == "n")
    # Loops through groups and adds mininum number of competitors per group
    for i in range(int(groups)):
        group = []
        for j in range(minCompetitorsPerGroup):
            if(labelGroupsByNumber):
                group.append(str(i + 1) + "-" + str(j + 1))
            else:
                group.append(chr(65 + i) + str(j + 1))
        groupOutput.append(group)

    # Section if there is an uneven number of groups
    if (minCompetitorsPerGroup != int(competitors) / int(groups)):
        # Index to start adding extra competitors
        startPoint = 0
        # Index to stop adding extra competitors
        endPoint = int(groups)
        # If smaller groups are first, start point changes
        if (smallerGroupsFirst):
            startPoint = int(groups) - (int(competitors) % int(groups))
        # If larger groups are first, end point changes
        else:
            endPoint = int(competitors) % int(groups)
        
        # For each group with an additional competitor, add new competitor placeholder
        for i in range(startPoint, endPoint):
            if(labelGroupsByNumber):
                groupOutput[i].append(str(i + 1) + "-" + str(len(groupOutput[i]) + 1))
            else:
                groupOutput[i].append(chr(65 + i) + str(len(groupOutput[i]) + 1))

    # Prints each item in list
    print("Group composition:")
    for i in groupOutput:
        print(i)

    printGroups(groupOutput)
    input("Complete, press enter to exit")

main()