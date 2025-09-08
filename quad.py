'''Program to calculate the real of a quadratic equation if there are any'''

import math
def roots():
    """
       This function takes the values of the quadratic equation and returns the roots

       Parameters:
           a (int): coefficient of x^2
           b (int): coefficient of x
           c (int): coefficient of 1

       Returns:
           Either no roots, one root or two real roots of the quadratic equation
       """
    print("Given a quadratic equation of the form a*x^2 + b*x + c")
    a = float(input("Please enter a: "))
    b = float(input("Please enter b: "))
    c = float(input("Please enter c: "))
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("There are 2 real solutions","\n","Solution 1:", "{:.2f}".format(root1), "\n","Solution 2:", "{:.2f}".format(root2))
    elif discriminant == 0:
        root = -b / (2*a)
        print("There is one real solution:", "{:.2f}".format(root))
    else:
        print("There are no real solutions")

roots()




