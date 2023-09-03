#Rough Draft
#Step 1: Create first list length 5
#Step 2: Create second list length 5
#Step 3: Find values that are exist in both list one and two. Store these in a new array(common list)
#Step 4: Remove repeats from array(common list)
#Step 5: Print out list one list two and common list


# List One
lone = []
print("List One. Enter 5 Ints")
for _ in range(5):
    value = int(input())
    lone.append(value)

#List Two
ltwo = []
print("List Two. Enter 5 Ints")
for _ in range(5):
    value = int(input())
    ltwo.append(value)


common_list = [value for value in lone if value in ltwo]
common_list = list(set(common_list))

#Print lists
print("List One:", lone)
print("List Two:", ltwo)
print("Common List:", common_list)
