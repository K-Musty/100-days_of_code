from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

MY_EMAIL = ""
MY_PASSWORD = ""
MY_NUMBER = ""

url = "https://www.linkedin.com"



service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get(url)
time.sleep(3)

try:
    sign_in = driver.find_element(By.LINK_TEXT, "Sign in")

    sign_in.click()


    time.sleep(2)

    input_email = driver.find_element(By.ID, "username")
    input_email.send_keys(MY_EMAIL)
    input_password = driver.find_element(By.ID, "password")
    input_password.send_keys(MY_PASSWORD)

    input_password.send_keys(Keys.RETURN)

    time.sleep(2)

    jobs = driver.find_element(By.XPATH, "//*[@id='global-nav']/div/nav/ul/li[3]/a")
    jobs.click()

    search = driver.find_element(By.CLASS_NAME, "jobs-search-box__text-input")
    search.send_keys("python developer")
    search.send_keys(Keys.ENTER)

    jobs_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
    jobs_apply.click()

    input_job = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
    input_job.send_keys(MY_NUMBER)

    next = driver.find_element(By.ID, "ember781")
    next.click()
    time.sleep(20)

finally:
    driver.quit()

