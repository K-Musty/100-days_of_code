import requests
from bs4 import BeautifulSoup


url = ""
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html-parser")




