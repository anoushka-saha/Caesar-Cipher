#Anoushka Saha
#Caesar Cipher Final
#May 8th, 2024

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

#Ask user if they want message encrypted or decrypted
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

#Ask user for message
message = input("Type your message:\n").lower()

#Ask user for amount of shift
shift = int(input("Type the shift number:\n"))

#Print new message
print("The new message is: " + caesar(direction, message, shift))


             