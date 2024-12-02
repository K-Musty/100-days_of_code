from selenium import webdriver
from selenium.webdriver.chrome.service import (Service)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

for i in range(100):
    cookie.send_keys(Keys)

driver.quit()

