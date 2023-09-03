
#def is used to assert a new function

#First we create a function that determines if a string
#exists as a suffix in another string. Returns either true or false

def findSuf(string1, string2):
    return string1.endswith(string2) or string2.endswith(string1)




#creating main function

def main():
    #allow user to input both strings
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    
    if findSuf(string1, string2):
        print("True")
    else:
        print("False")



if __name__ == "__main__":
    main()