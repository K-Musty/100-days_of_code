from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

MY_EMAIL = ""
MY_PASSWORD = ""


url = "https://www.linkedin.com"



service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get(url)
time.sleep(3)

try:
    sign_in = driver.find_element(By.LINK_TEXT, "Sign in")

    sign_in.click()


    time.sleep(20)

    input_email = driver.find_element(By.ID, "username")
    input_email.send_keys(MY_EMAIL)
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys(MY_PASSWORD)

    input_password.send_keys(Keys.RETURN)

    time.sleep(10)

finally:
    driver.quit()

