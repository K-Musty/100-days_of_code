#!/usr/bin/python3
#Function with Outputs

def format_name(f_name, l_name):
    first = f_name.title()
    last = l_name.title()
    return f"{first} {last}"
formated_string = format_name("AbbaA", "ABBAA")
print(formated_string)
