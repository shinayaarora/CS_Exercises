#1. Setup
amount = int(input('Please enter the amount of money you wish to withdraw: ')) #Taking input from user
fewest_bills_dict = {} #Creating a dictionary to save the bill count

#2. Processing the information
def fewest_bills(amount, fewest_bills_dict): #Creating a function to calculate the fewest bills
    denominations = [100, 50, 20, 10, 5, 1]  #A list with all denominations
    for i in denominations:                  #Calculating the number of bills for each denomination
        bills = amount // i
        fewest_bills_dict[i] = bills
        amount = amount - bills * i          #Changing the amount


def result(fewest_bills_dict):               #Creating a function to print the results
    for i in fewest_bills_dict:
        if i == 100:
            x = 'hundred(s)'
        elif i == 50:
            x = 'fifty(s)'
        elif i == 20:
            x = 'twenty(s)'
        elif i == 10:
            x = 'ten(s)'
        elif i == 5:
            x = 'five(s)'
        elif i == 1:
            x = 'one(s)'
        print('You received', fewest_bills_dict[i], x)

fewest_bills(amount, fewest_bills_dict)
result(fewest_bills_dict)