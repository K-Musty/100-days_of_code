# import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

comm_portal = driver.find_element(By.PARTIAL_LINK_TEXT, value="Community portal")
# comm_portal.click()

try:
    search = driver.find_element(By.NAME, "search")
    search.send_keys("Python")
    search.send_keys(Keys.ENTER)
    print("Search executed successfully!")
except Exception as e:
    print(f"An error occurred: {e}")


input("Press Enter to close the browser...")
# or
# time.sleep(10)

# print(article_count.text.split()[0])


driver.quit()