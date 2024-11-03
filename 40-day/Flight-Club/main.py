print("Welcome to KMusty's Flight Club !!\n"
      "We find the best flight deals and email you")

first_name = input("Insert your first name")
last_name = input("Insert your last name")
while True:
    first_email = input("Insert your email")
    second_email = input("please insert your email for confirmation")

    if first_email == second_email:
        print("Your now in the club !!!")
        break