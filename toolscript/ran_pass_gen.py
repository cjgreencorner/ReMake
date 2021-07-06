#!/usr/bin/env python
"""""""""""""""""""""
Random password generator
"""""""""""""""""""""
# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Finished"

# IMPORTS
import random
import string

def random_wachtwoord(letters, cijfers):

    string_1 = ''.join((random.choice(string.ascii_letters) for i in range(letters)))

    string_1 += ''.join((random.choice(string.digits) for i in range(cijfers)))
    lijst = list(string_1)
    random.shuffle(lijst)
    string_2 = ''.join(lijst)
    return string_2

def main():
    try:
        print("Make a choice (1 or 2).")
        print("1 = Normal password")
        keuze = int(input("2 = Strong password: "))
        if keuze == 1:
            print("Normal password:", random_wachtwoord(6, 2))

        elif keuze == 2:
            print("Strong password:", random_wachtwoord(7, 4))

        elif keuze != '1' or '2':
            print("Choose a number between 1 or 2.")
            main()

    except ValueError: 
        print("Numbers only.")
        main()


if __name__ == '__main__':
    main()
