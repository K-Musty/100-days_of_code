import requests
from bs4 import BeautifulSoup
import selenium


FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfHIGjkwmjrfMmf9R49C-dOSkqYukzaWwA6hOgGIYYDgXgigQ/viewform?usp=header"
base_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.zillow.com/",
    "Connection": "keep-alive",
}

response = requests.get(url=base_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
addresses = []
all_links = []
prices = []
# print(soup)
listings = soup.find_all('li', class_='ListItem-c11n-8-107-0__sc-13rwu5a-0 StyledListCardWrapper-srp-8-107-0__sc-wtsrtn-0 dAZKuw xoFGK')
# links = soup.find_all('a', class_='StyledPropertyCardDataArea-c11n-8-107-0__sc-10i1r6-0 iwOFcv property-card-link')
# amounts = soup.find_all('span', class_="Text-c11n-8-107-0__sc-aiai24-0 PropertyCardInventoryBox__PriceText-srp-8-107-0__sc-1jotqb7-3 eawGuS kgaGKJ")

for listing in listings:
    print(listing.prettify())
    url = listing.getText("url")
    all_links.append(url)
    name = listing.getText("name")
    addresses.append(name)
print(all_links)
