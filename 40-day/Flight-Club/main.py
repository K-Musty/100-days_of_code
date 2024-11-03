print("Welcome to KMusty's Flight Club !!\n"
      "We find the best flight deals and email you")

first_name = input("Insert your first name\n")
last_name = input("Insert your last name\n")
while True:
    first_email = input("Insert your email\n")
    second_email = input("please insert your email for confirmation\n")

    if first_email == second_email:
        print("Your now in the club !!!")
        break
    else:
        print("Email doesn't match try again")