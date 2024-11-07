import requests
url = "sheety api"
headers = {
    "Authorization": ""
}

print("Welcome to K-Musty's Flight Club !!\n"
      "We find the best flight deals and email you")

first_name = input("Insert your first name \n")
last_name = input("Insert your last name \n")
while True:
    first_email = input("Insert your email \n")
    second_email = input("please insert your email for confirmation\n")

    if first_email == second_email:
        parameters = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": first_email
            }
        }
        response = requests.post(url=url, json=parameters, headers=headers)
        response.raise_for_status()
        print(response.status_code)
        print("Your now in the club !!!")
        break
    else:
        print("Email doesn't match try again\n")