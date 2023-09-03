#Get user input/print instructions
#Split input into list of individual characters
#Group the characters into 3 
#Put all groups of three back together

owords = input("Enter a string: ")


def split_lists(input_string, chunk_size):
    char_array = list(input_string)
    list_of_lists = [char_array[i:i + chunk_size]
                    for i in range(0, len(char_array), chunk_size)]
    return list_of_lists

chunk_size = 3

#Get final list/print it
result = split_lists(owords, chunk_size)
print(result)
