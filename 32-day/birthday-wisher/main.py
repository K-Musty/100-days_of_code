##################### Extra Hard Starting Project ######################
import pandas
import datetime
import random
import smtplib

with open("letter_templates/letter_1.txt") as file_1:
    letter_1 = file_1.read()

with open("letter_templates/letter_2.txt") as file_2:
    letter_2 = file_2.read()

with open("letter_templates/letter_3.txt") as file_3:
        letter_3 = file_3.read()
letters = [letter_1, letter_2, letter_3]

# 1. Update the birthdays.csv
data  = pandas.read_csv("birthdays.csv")
# new_data = {
#     "name": "Zayyad",
#     "email": "muhammadzayyad709@gmail.com",
#     "year": 2003,
#     "month": 2,
#     "Day": 17
# }
# new_entry = pandas.DataFrame([new_data])
# new_entry.to_csv("birthdays.csv", mode="a", header=False, index=False)


# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
day = today.day
month = today.month
my_email = "johnnymont2255@gmail.com"
password = "ayrghhhjgmcenzfh"

for (key, item) in data.iterrows():
    if int(item["month"]) == month and int(item["day"]) == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        name_word = "[NAME]"
        random_letter = random.choice(letters)
        final_letter = random_letter.replace(name_word, item["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP_SSL("SMTP.gmail.com", 465) as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=item["email"], msg="Subject:Happy Birthday\n\n"
                                                                                f"{final_letter}")







