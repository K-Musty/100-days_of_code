from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
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

    search = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
    search.send_keys("python developer")
    search.send_keys(Keys.ENTER)

    job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
    for job in job_listings:
        job.click()
        time.sleep(2)

        try :

            jobs_apply = driver.find_element(By.CLASS_NAME, "afaFOTlZPsCzjvRLucMiKLrwEMAMHRDLkDjhg")
            jobs_apply.click()


            input_job = driver.find_element(By.CLASS_NAME, "artdeco-text-input--input")
            if input_job.text == "" :
                input_job.send_keys(MY_NUMBER)

            next_next = driver.find_element(By.ID, "ember781")
            next_next.click()

            follow_button = driver.find_element(by=By.CLASS_NAME, value="follow")
            follow_button.click()

            time.sleep(20)


        except NoSuchElementException:

            print("No application button, skipped.")

            continue


finally:
    driver.quit()

