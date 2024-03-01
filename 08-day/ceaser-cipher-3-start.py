#!/usr/bin/python3
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: "))

#Don't change the code above 👆
def ceaser(text_field, shift_field, cipher_direction):
    end_text = ""
    for letter in text_field:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            new_position = position + shift_field
            new_letter = alphabet[new_position]
            end_text += new_letter
        elif cipher_direction == "decode":
            new_position = position - shift_field
            new_letter = alphabet[new_position]
            end_text += new_letter
    print(f"The {cipher_direction}d text is {end_text}")
ceaser(text, shift, direction)
