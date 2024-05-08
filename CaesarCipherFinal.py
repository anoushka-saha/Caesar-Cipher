#Anoushka Saha
#Caesar Cipher Final
#May 8th, 2024
#Day 8 Final Project

#Defining the function that will do both encryption and decryption
def caesar(choice, text, num):
    caesar_text = ""
    for i in range(len(text)):
        if choice == "encode":
            new_ascii = ord(text[i]) + num
            if new_ascii > ord('z'):
                    new_ascii -= 26
        elif choice == "decode":
            new_ascii = ord(text[i]) - num
            if new_ascii > ord('z'):
                    new_ascii += 26

        caesar_text += chr(new_ascii)

    return caesar_text

#Loop so user can continue using program
while True: 
    #Ask user if they want message encrypted or decrypted
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    #Ask user for message
    message = input("Type your message:\n").lower()

    #Ask user for amount of shift
    shift = int(input("Type the shift number:\n"))

    #Print new message
    print("The new message is: " + caesar(direction, message, shift))

    #Check if user wants to go again
    go_again = input("Do you want to go again? (yes/no):\n")

    #Breaking loop if user wants to exit program
    if go_again.lower() != "yes":
         break


             