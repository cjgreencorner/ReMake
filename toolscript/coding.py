#!/usr/bin/env python
"""""""""""""""""""""""""""""""""""""""
# A console to encrypt and decrypt text #
"""""""""""""""""""""""""""""""""""""""
# IMPORTS
import decoder

# AUTHORINFO
_author_ = "Joel Chapon"
_email_ = "joel.chapon@student.kdg.be"
_status_ = "Finished"

# FUNCTIONS
def main():
    print('Encoder & decoder.')
    print('\n1 = Encode text') # Give the user 3 choices
    print('2 = Decode text')
    print('3 = Show history')
    try:
        choice = int(input("Make a choice: ")) # Ask the user for a number
        if choice == 1:
            print('Encode')
            print('1 = Encode a word') # Give the user 3 subchoices
            print('2 = Encode a textfile')
            print('3 = Return')
            choice2 = int(input("Make a choice: "))
            if choice2 == 1:
                print('Encode a word')
                code = input("Which word would you like to hide? ")
                encoded = decoder.get_code(code)
                print(code, "=", encoded)
                history = ["Encrypted:\n", code, '  =  ', encoded, "\n\n"]
                f = open('history.txt', 'a')  # Open the history file
                f.writelines(history)  # Write the word down in the history.txt file
                f.close()  # Close the file
                input("Press enter to continue.")  # Used for a pause
                main() # Return to the menu
            elif choice2 == 2:
                print('Encode a textfile')
                print('Example: python/examples/normal')
                path = input("Enter the path of the textfile: ")  # Ask the user for the path
                f = open(path, 'r')  # Open the path
                data = f.read()
                encoded = decoder.get_code(data)
                print(data, '=', encoded)
                history = ["Encrypted a textfile:\n", path, "\n\n"]
                h = open('history.txt', 'a')
                h.writelines(history)
                h.close()
                f.close()
                input("Press enter to continue.")
                main()
            elif choice2 == 3:
                main()
            elif choice != 1 or choice != 2 or choice != 3: # Check if one of the three numbers are given
                print('Choose a number between 1 and 3.')

        elif choice == 2:
            print('Decode')
            print('1 = Decode a word')
            print('2 = Decode a textfile')
            print('3 = Return')
            choice2 = int(input("Make a choice: "))  # Ask the user for a number
            if choice2 == 1:
                print('Decode a word')
                word = input("Which word would you like to decode? ")
                decoded = decoder.get_decode(word)
                print(word, '=', decoded)
                history = ["Decrypted:\n", decoded, '  =  ', word, "\n\n"]
                f = open('history.txt', 'a')
                f.writelines(history)
                f.close()
                input("Press enter to continue.")
                main()
            elif choice2 == 2:
                print('Decode a textfile')
                print('Example: python/examples/encoded')
                path = input("Enter the path of the textfile: ")  # Ask the user for the path
                f = open(path, 'r')
                data = f.read()
                decoded = decoder.get_decode(data)
                print(data, '=', decoded)
                history = ["Decrypted a textfile:\n", path, "\n\n"]
                h = open('history.txt', 'a')
                h.writelines(history)
                h.close()
                f.close()
                input("Press enter to continue.")
                main()
            elif choice2 == 3:
                main()
            elif choice != 1 or choice != 2 or choice != 3: # Check if one of the three numbers are given
                print('Choose a number between 1 and 3.')

        elif choice == 3:
            show_history()
            main()
        elif choice != 1 or choice != 2 or choice != 3: # Check if one of the three numbers are given
            print('Choose a number between 1 and 3.')
    except ValueError: # If someone doesn't write a number
        print("Number expected.")
        main()

def show_history():
    f = open("history.txt", "r")
    data = f.read()
    print('\nHistory:\n')
    print(data)
    f.close()
    input("Press enter to continue.")


if __name__ == '__main__':
    main()
