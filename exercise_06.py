#thought proess: 
#Step one: Get row num 1-5 from user
#Step two: Get col num 1-5 from user
#Step three: Print 5 rows 5 columns of zero
#Step four: replace entered col/row w a 1

#creating rows and columns using for loop (the "end=' '" creates spacer)
def print_grid(row, column):
    if 1 <= row <= 5 and 1 <= column <= 5:
        for i in range(1, 6):
            #Calculate if printing a 1 or 0 depending on what user input row and col as
            for j in range(1, 6):
                if i == row and j == column:
                    print(1, end='|')
                else:
                    print(0, end='|')
            print()
    else:
        print("Row and column numbers should be between 1 and 5 inclusive.")

row = int(input("Enter the row number (1-5): "))
column = int(input("Enter the column number (1-5): "))

print_grid(row, column)
