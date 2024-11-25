import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
# from fake_useragent import UserAgent
my_email = ""
password = ""


URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers= {
    "User-Agent": "",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
    "Accept-Encoding": "gzip, deflate, br, zstd"
}
response = requests.get(url=URL, headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find(name="span", class_="a-price-whole")
price_value = float(price.getText().strip("$")[1])

print(price_value)
if price_value < 100:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as mail_connection:
        mail_connection.starttls()
        mail_connection.login(user=my_email, password=password)
        mail_connection.sendmail(from_addr=my_email, to_addrs="kmustapha9564@gmail.com",
                                 msg="Subject:Sales Alert!!!!\n\n\n Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker,"
                                     " Slow Cooker, Rice Cooker, Steamer, Sauté, Yogurt Maker, Warmer & Sterilizer, "
                                     "Includes App With Over 800 Recipes, Stainless Steel, 3 Quart\n "
                                     "Is Now At an Affordable price".encode("utf-8"))

