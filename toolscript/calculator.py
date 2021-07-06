#!/usr/bin/env python
##########################################
#          Calculator Version 3          #
##########################################

# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"


# +
def plus(x, y):
    return x + y

# -
def min(x, y):
    return x - y

# *
def maal(x, y):
    return x * y

# /
def delen(x, y):
    return x / y



def main():
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    try:

        keuze = int(input("Make your choice (1/2/3/4): "))

        if keuze == 1 or keuze == 2 or keuze == 3 or keuze == 4:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if keuze == 1:
                print(num1, "+", num2, "=", plus(num1, num2))

            elif keuze == 2:
                print(num1, "-", num2, "=", min(num1, num2))

            elif keuze == 3:
                print(num1, "*", num2, "=", maal(num1, num2))

            elif keuze == 4:
                print(num1, "/", num2, "=", delen(num1, num2))


        elif keuze != 1 or keuze != 2 or keuze != 3 or keuze != 4:

            print("Please enter a number between 1 and 4.")
            main()

    except ValueError: 
        print("Only numbers please.")
        main()


if __name__ == '__main__':
    main()
