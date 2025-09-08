'''Program that recommends whether it is beneficial to pay your loans before investing or if you should only make the minimum payments and invest the rest.  '''
def invest(loans, annual_interest_rate, minimum_payment,monthly_payment, current_age, retirement_age,annual_return_rate):
    '''
    Parameters: (All >= 0)
     loans: money you owe in loans
     annual_interest_rate: annual interest rate of the loans
     minimum_payment: minimum monthly loan payment
     monthly_payment: money you will be putting towards loans/retirement each month (>= minimum payment)
     current_age
     retirement_age
     annual_return_rate: predicted annual rate of return

    Returns:
     The recommendation if one should pay loans before investing or make minimum payments and invest the rest
    '''
    monthly_interest_rate = annual_interest_rate/12
    monthly_investment_rate = annual_return_rate/12

    amount_balance = loans
    investment = 0
    amount_balance_2 = loans
    investment_2 = 0

    for i in range((retirement_age - current_age) * 12):
        # Apply interest at the start of each month
        if amount_balance > 0:
            amount_balance *= (1 + monthly_interest_rate)
        investment *= (1 + monthly_investment_rate)

        if amount_balance_2 > 0:
            amount_balance_2 *= (1 + monthly_interest_rate)
        investment_2 *= (1 + monthly_investment_rate)

        # Deduct payments and invest the rest
        payment_1 = min(amount_balance, minimum_payment)
        amount_balance = amount_balance - payment_1
        investment = investment + (monthly_payment - payment_1)

        # Pay off as much of the loan as possible, then invest
        payment_2 = min(amount_balance_2, monthly_payment)
        amount_balance_2 = amount_balance_2 - payment_2
        if amount_balance_2 <= 0:
            investment_2 = investment_2 + monthly_payment - payment_2

    investment -= max(0, amount_balance)
    investment_2 -= max(0, amount_balance_2)

    if investment >= investment_2:
        print("You should only make minimum payments on your loans and invest the rest")
        return f"If you do you will have ${investment:.2f} as opposed to ${investment_2:.2f} when you retire."
    else:
        print("You should pay of all of your loans before you start investing")
        return f"If you do you will have ${investment_2:.2f} as opposed to ${investment:.2f} when you retire."


def valid_input(input_val, str):
    '''
    Parameters: (input_val, str)
     input_val: the input value
     str: the input string

    Returns:
        the input converted to float if it is valid
    '''
    if input_val < 0:
        while (input_val < 0):
            input_val = float(input(str))

    return input_val


def main():
    '''
    Main function: takes all the input and calls the invest function
    '''
    loans = float(input("Enter how much money you owe in loans: "))
    loans = valid_input(loans, "Enter how much money you owe in loans: ")

    annual_interest_rate: float = float(input("Enter the annual interest rate of the loans: "))
    annual_interest_rate = valid_input(annual_interest_rate, "Enter the annual interest rate of the loans: ")

    minimum_payment = float(input("Enter your minimum monthly loan payment: "))
    minimum_payment = valid_input(minimum_payment, "Enter your minimum monthly loan payment: ")

    monthly_payment = float(
        input("Enter how much money you will be putting towards loans/retirement each month: "))
    if monthly_payment < minimum_payment:
        while (monthly_payment < minimum_payment):
            monthly_payment = float(input("Enter how much money you will be putting towards loans/retirement each month: "))

    current_age_float = float(input("Enter your current age: "))
    current_age_float = valid_input(current_age_float, "Enter your current age: ")
    current_age = int(current_age_float)

    retirement_age_float = float(input("Enter the age you plan to retire at: "))
    if retirement_age_float < current_age_float:
        while (retirement_age_float < current_age_float):
            retirement_age_float = float(input("Enter the age you plan to retire at: "))

    retirement_age = int(retirement_age_float)


    annual_return_rate = float(input("Enter your predicted annual rate of return: "))
    annual_return_rate = valid_input(annual_return_rate, "Enter your predicted annual rate of return: ")

    print(invest(loans, annual_interest_rate, minimum_payment, monthly_payment, current_age, retirement_age,annual_return_rate))
    print("")


main()
