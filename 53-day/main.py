import requests
from bs4 import BeautifulSoup


base_url = "https://www.zillow.com/homes/for_rent/"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html-parser")




