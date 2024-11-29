from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
events = {}

event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

event_date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for i in range(len(event_date)):
    events[i] = {
        "time": f"2024-{event_date[i].text}",
        "name": event_name[i].text
    }


print(events)

driver.quit()