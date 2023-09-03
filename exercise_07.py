#Output message w insutrction and take input
#create list of input from user of numbers
#Use ''while' to determine when to stop this loop
#Break loop when user inputs "QUIT"
#Div int of list all number to determine which are even
#Store even on new Even list
#Print both lists


all_numbers = []
even_numbers = []

#Run While loop for input until "QUIT"(break)
while True:
    user_input = input("Enter an integer (or type 'QUIT' to exit): ")
    if user_input == "QUIT":
        break
    try:
        num = int(user_input)
        all_numbers.append(num)
    #Evens
        if num % 2 == 0:
            even_numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer or 'QUIT'.")

# Print both lists
print("All numbers:", all_numbers)
print("Even numbers:", even_numbers)
