#determining steps:
#Step 1: Input a value from user. store as value(n)
#Step 2: Create a list with length n
#Step 3: Loop through list and have user input a value for each list item

#Take input
def main():
    n = int (input("Enter a number: "))
    numbers = []
#create an empty list

#loop through range of n. print out/take input for each number
    for i in range(n):
        num = float(input(f"Enter a float {i+1}: "))
        #add number to list(end of list)
        numbers.append(num)

#print out completed list
    print("List:", numbers)

#Calculate mean and print it out as long as n > 0
    if n > 0:
        mean = sum(numbers) / n
        print("Average:", mean)
    else:
        print("No numbers entered.")

if __name__ == "__main__":
    main()
