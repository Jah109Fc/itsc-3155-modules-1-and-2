def shift_lowercase_to_front(input_str):
    lowercase_chars = ""
    uppercase_chars = ""
    
    # Separate lowercase and uppercase characters
    for char in input_str:
        if char.islower():
            lowercase_chars += char
        elif char.isupper():
            uppercase_chars += char
    
    # Combine the lowercase and uppercase characters
    result_str = lowercase_chars + uppercase_chars
    
    return result_str

# Get input from the user
user_input = input("Enter a string: ")

# Call function and print result
result = shift_lowercase_to_front(user_input)
print("Transformed string:", result)