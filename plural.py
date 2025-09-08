'''Program to change a noun to its plural form'''
def plural():
    '''Function to convert a noun to its plural form
    Parameters:
           noun: a noun entered by the user which will b e converted to its plural form
    Returns:
           plural of the noun
    '''
    noun = str(input('Please enter a word: ')) #Asking the user for a noun
    og_noun = noun
    #Conditions for making the plural of a given noun
    if noun.endswith(('ch', 'sh', 's', 'x', 'z')):
        noun += 'es'
    elif noun.endswith('y') and noun[-2] not in 'aeiou':
        noun = noun[:-1] + 'ies'
    elif noun.endswith(('f','fe')):
        if noun.endswith('f'):
            noun = noun[:-1] + 'ves'
        elif noun.endswith('fe'):
            noun = noun[:-2] + 'ves'
    else:
        noun = noun + 's'
    print(f'The plural form of {og_noun} is {noun}.') #Printing the noun
plural()  #Calling the function
