# PythonGroupGenerator
This is a Python script designed for users to generate a set of unique placeholders for a round-robin tournament involving multiple groups. This may be expanded to generate a match schedule based on user input

**Important**: the script may output items in the format of 1-1, 1-2, etc. and when saved as a CSV file, may be rendered as dates when viewed in an application like Excel.

## How to use the script
1. When running the script, you will be asked to input the number of competitors and groups you want to create. Input is valid when:
    - The number of competitors is 3 or more
    - The number of groups is 1 or more
    - The number of competitors divided by groups is 3 or more
2. If the groups will have an unequal number of competitors, you will be asked whether to have groups with the larger or smaller number of competitors placed first.
3. If there are 26 or fewer groups, you will be asked whether to label groups by letters (e.g., A1, A2) or numbers (e.g., 1-1, 1-2).
4. The script will generate the groups and positions based on your input and print out the groups as list items, then in a CSV format.
