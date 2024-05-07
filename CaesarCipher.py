alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, num):
    cipher_text = ""
    for i in range(len(message)):
        if message[i].isalpha():
            # Calculate the new ASCII value after shifting by num
            new_ascii = ord(message[i]) + num
            # Handle wrapping around the alphabet for uppercase letters
            if message[i].isupper():
                if new_ascii > ord('Z'):
                    new_ascii -= 26
            # Handle wrapping around the alphabet for lowercase letters
            elif message[i].islower():
                if new_ascii > ord('z'):
                    new_ascii -= 26
            # Convert the new ASCII value back to a character
            cipher_text += chr(new_ascii)
        else:
            # Append non-alphabetic characters as is
            cipher_text += message[i]
    return cipher_text

print("The encrypted word is " + encrypt(text, shift))