import requests
from bs4 import BeautifulSoup


base_url = ""
parameters = {
  
}

response = requests.get(url=url)
soup = BeautifulSoup(response.text, "html-parser")




