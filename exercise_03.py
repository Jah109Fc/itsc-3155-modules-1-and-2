#take an integer input from the termal. the input is assigned text inside ""
x = int(input("Enter an integer greater than 1: "))

#ensure x is greater than 1
if x <=1:
    print("Must be an INTEGER GREATER than ONE")

#loop through zero to x and print the cubed value of each number
else:
    for i in range(x+1):
        print(f"The cube of {i} is {i ** 3}")