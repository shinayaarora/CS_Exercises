
#1. Setup
string = str(input("Please enter a string: "))  # Asking the user to input a string
def capitalize(string):        #Creating a function
    vowels = 'AEIOUaeiou'      #Creating a list of vowels
    modified_string = ''         #Creating an empty string
#2. Go through each letter of the sentence/word
    for letter in string:      #for loop
#3. Detecting all the vowels and the consonants
#4. Making all the vowels uppercase and all consonants lowercase
        if letter in vowels:
            modified_string = modified_string + letter.upper()   #if letter is vowel, change to uppercase and add to string
        elif letter not in vowels:
            modified_string = modified_string + letter.lower()   #if letter is consonant, change to lowercase and add to string
# 5. Result:
    return modified_string       #Return the modified string

print(capitalize(string))
