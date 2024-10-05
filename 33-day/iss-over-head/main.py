import requests
from datetime import datetime
import smtplib
import time

my_email = "johnnymont2255@gmail.com"
password = "ayrghhhjgmcenzfh"

MY_LAT = 11.999970
MY_LONG = 8.534860

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:

    #If the ISS is close to my current position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        # and it is currently dark
        if sunset >= time_now.hour or sunrise <= time_now.hour:
            # Then email me to tell me to look up.
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs="kmustapha559@gmal.com",
                                    msg="Subject: ISS over head\n\n"
                                        "Go out and look up!!!")
    # BONUS: run the code every 60 seconds.
    time.sleep(60)





