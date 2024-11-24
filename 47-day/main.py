import requests
from bs4 import BeautifulSoup
import lxml
# from fake_useragent import UserAgent

URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers= {
    "User-Agent": "",
    "Accept-Language": "",
    "Accept": "",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/",
    "Accept-Encoding": ""
}
response = requests.get(url=URL, headers=headers)
# print(response.text)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find(name="span", class_="a-price-whole")
print(price.prettify())