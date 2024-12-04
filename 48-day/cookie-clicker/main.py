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





def get_current_money():
    money_text = money.text.replace(",", "")
    return int(money_text) if money_text.isdigit() else 0

def get_cookies_per_second():
    cps_element = driver.find_element(By.ID, "cps")
    return cps_element.text


time_skip = time.time() + 5
end_time = time.time() + 15

while True:

    cookie.click()


    if time.time() > time_skip:
        current_amount = get_current_money()
        prices_affordable = []
        right_panel = driver.find_elements(By.CSS_SELECTOR, "#store div")

        for i in right_panel:
            item_text = i.text
            if "-" in item_text:
                item_price = int(item_text.split("-")[1].split("\n")[0].strip().replace(",", ""))
                if item_price <= current_amount:
                    prices_affordable.append((item_price, i))
                    # print(item_price)

        if prices_affordable:

            max_price = 0
            most_expensive_item = None

            # Manually find the most expensive item
            for price, item in prices_affordable:
                if int(price) > int(max_price):
                    max_price = price
                    most_expensive_item = item

            # Click the most expensive item
            if most_expensive_item:
                most_expensive_item.click()

        time_skip = time.time() + 5

    if time.time() > end_time:
        print(f"Cookies per second is: {get_cookies_per_second()}")
        break


driver.quit()
