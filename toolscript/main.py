#!/usr/bin/env python
"""""""""""""""""""""
This is a multifunctional Python script for Raspberry Pi.
"""""""""""""""""""""
# IMPORTS
import calculator, ran_pass_gen, coding, bash, time


# AUTHORINFO
__author__ = "Joel Chapon"
__email___ = "joel.chapon@student.kdg.be"
__status__ = "Finished"


# FUNCTIONS
def main():
    print("\n1 = Update your system")
    print("2 = Install a package")
    print("3 = Basic calculator")
    print("4 = Print basic system information")
    print("5 = Generate a random password")
    print("6 = Encode or decode a word")
    print("7 = Shutdown the Raspberry Pi")

    try:
        choice = int(input("Make a choice: ")) # Ask the user for a number
    except ValueError:  # If the user gives something else then a number.
        print("Please give a number!")
        main()
    if choice == 1: # This happens if the user chose the first function
        bash.call_update()
        main() # Go back to the main function
    if choice == 2:
        bash.install_package()
        time.sleep(5)
        main()
    if choice == 3:
        calculator.main()
        time.sleep(5)
        main()
    if choice == 4:
        bash.show_info()
        time.sleep(5)
        main()
    if choice == 5:
        ran_pass_gen.main()
        time.sleep(5)
        main()
    if choice == 6:
        coding.main()
        time.sleep(5)
        main()
    if choice == 7:
        bash.call_shutdown()
    else: # If the user picks another number.
        print('Pick a number between 1 and 7...')
        main()

    # except ValueError: # If the user gives something else then a number.
    #     print("Please give a number!")
    #     main()



if __name__ == '__main__':
    main()
