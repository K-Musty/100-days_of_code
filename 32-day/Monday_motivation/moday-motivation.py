import pandas
import smtplib
import datetime
import random

with open("quotes.txt", mode="r") as file:
    quotes = file.readlines()
quotes_list = pandas.Series(quotes)
date = datetime.datetime.now()

my_email = "johnnymont2255@gmail.com"
password = "ayrghhhjgmcenzfh"
connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
connection.login(user=my_email, password=password)
random_quotes = random.choice(quotes_list)
if date.weekday() == 0:
    connection.sendmail(from_addr=my_email, to_addrs="lemonpart@yahoo.com",
                        msg=f"Subject:Monday motivation\n\n {random_quotes}")

connection.close()
