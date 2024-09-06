# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt", mode="r") as names:
    name_list = names.readlines()
with open("Input/Letters/starting_letter.txt", mode="r") as letters:
    letter = letters.read()
    for name in name_list:
        split_name = name.split()
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as sent:
            sent.write(new_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
