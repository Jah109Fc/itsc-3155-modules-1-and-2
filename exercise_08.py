#Get input for 10 ints
#Store input in original list
#Use 'count' to determine occurances of each int in original list
#If 'count' for given int equals 1 add to new 'even' list


#create orginal list
input_list = []
for i in range(10):
    num = int(input(f"Enter integer {i+1}: "))
    input_list.append(num)
#Calculate evens and make 'even' list
unique_elements = []
for num in input_list:
    if input_list.count(num) == 1:
        unique_elements.append(num)

# Print both lists
print("Original list:", input_list)
print("List with unique elements:", unique_elements)

