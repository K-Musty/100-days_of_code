from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service



url = ""



service = Service(url)
driver = webdriver.Chrome(service=service)

driver.find_element()

