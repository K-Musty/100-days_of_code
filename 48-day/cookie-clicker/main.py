import time

from selenium import webdriver
from selenium.webdriver.chrome.service import (Service)
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys



service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, "money")
right_panel = driver.find_elements(By.CSS_SELECTOR, "#store div")



def get_current_money():
    money_text = money.text
    return int(money_text.replace(",","")) if money_text.isdigit() else 0


time_skip = time.time() + 5

while True:

    cookie.click()

    if time.time() > time_skip:
        current_amount = get_current_money()

        for item in right_panel:
            item_price = item.text.replace(",", "")

            if int(item_price) <= int(current_amount):
                item.click()
                time_skip = time_skip + 5

        time.sleep(0.5)

    driver.quit()

