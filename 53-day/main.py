import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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

prices = []
all_links = []


links = soup.find_all("a", {"class": "property-card-link"})

for link in links:
    yes = link.get('href')
    all_links.append(yes)

find_addresses = soup.find_all(name="address")

addresses = [adds.text for adds in find_addresses]
find_price = soup.find_all("div", {"class": "PropertyCardWrapper__StyledPriceGridContainer-srp-8-109-1__sc-16e8gqd-0 QNjBw"})
for price in find_price:
    price_text = price.text
    stripped = price_text.strip("+/mo")
    prices.append(stripped)


# Selenium form automation
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)



for item in range(len(prices)):
    driver.get(FORM_URL)
    time.sleep(4)
    form_input = driver.find_elements(By.CLASS_NAME,"Xb9hP")

    form_input[0].send_keys(addresses[item])
    form_input[1].send_keys(prices[item])
    form_input[3].send_keys(links[item])

    time.sleep(3)

    submit_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
    next_session = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    time.sleep(3)

driver.quit()


