from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.ID, value="articlecount")
print(article_count.text.split()[0])
driver.quit()