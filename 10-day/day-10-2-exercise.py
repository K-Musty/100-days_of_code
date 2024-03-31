#!/usr/bin/python3
#Function with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didnt provide inputs"
    first = f_name.title()
    last = l_name.title()
    return f"{first} {last}"
formated_string = format_name(input("What is your first Name"), input("what is your last name?"))
print(formated_string)

