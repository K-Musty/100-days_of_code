#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://tinder.com/")

EMAIL = "kmustapha559@gmail.com"
PASSWORD = "07046989916kallikadi"

accept = driver.find_element(By.CLASS_NAME, "lxn9zzn")
accept.click()

login = driver.find_element(By.XPATH, "//*[@id='q2098069830']/div/div[1]/div/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]")
login.click()

time.sleep(3)


facebook = driver.find_element(By.XPATH, "//*[@id='q369688754']/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div[2]/div/div")
facebook.click()
time.sleep(3)

# Switching windows
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)

email = driver.find_element(By.ID, "email")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Switching windows back
driver.switch_to.window(base_window)
print(driver.title)

location = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[1]')
location.click()
time.sleep(5)

notification = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div/div/div[3]/button[2]')
notification.click()
time.sleep(5)

night_mode = driver.find_element(By.XPATH, value='/html/body/div[2]/main/div/div[2]/button')
night_mode.click()

for num in range(101):

    time.sleep(3)

    try:
        like = driver.find_element(By.XPATH, "")
        like.click()
        print("Liked !!!!!")

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()
            print("A Match !!!!")

        except NoSuchElementException:
            time.sleep(3)

        else:
            driver.quit()
            break

driver.quit()

