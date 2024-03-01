#!/usr/bin/python3
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: "))

#Don't change the code above 👆
def encrypt (text_field, shift_field):
    cipher_text = ""
    for letter in text_field:
        position = alphabet.index(letter)
        new_position = position + shift_field
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(cipher_text)

def decrypt(text_field, shift_field):
    decipher_text = ""
    for letter in text_field:
        position = alphabet.index(letter)
        new_position = position - shift_field
        decipher_text += alphabet[new_position]
    print(decipher_text)

if direction == "encode":
    encrypt(text_field=text, shift_field=shift)
elif direction == "decode":
    decrypt(text_field=text, shift_field=shift)

