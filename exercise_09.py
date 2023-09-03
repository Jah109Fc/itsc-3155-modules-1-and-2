#Print instructions and get input for 5 words
#Store words in a list
#Print out the words from the list using 'joinwor'


#Print insutructions to user/get input(5 words)
#Add input words to 'words' string
words = []
for _ in range(5):
    word = input("Enter a word: ")
    words.append(word)


# Create a single string from the words
spaced_string = ' '.join(words)

# Print result
print("Words list:", words)
print("Spaced string:", spaced_string)
