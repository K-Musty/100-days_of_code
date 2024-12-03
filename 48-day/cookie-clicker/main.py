from selenium import webdriver
from selenium.webdriver.chrome.service import (Service)
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, "money")
right_panel = driver.find_elements(By.CLASS_NAME, "amount")

action = ActionChains(driver)

def get_current_money():
    money_text = money.text
    return money_text.replace(",","")


for i in range(100):

    action.click(cookie).perform()
    current_amount = get_current_money()

    for item in right_panel:
        item_price = item.text.replace(",", "")

        if int(item_price) <= int(current_amount):
            item.click()





driver.quit()

