#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("/usr/local/bin/chromedriver")

driver = webdriver.Chrome(service=service)

driver.get("https://tinder.com/")

login = driver.find_element(By.LINK_TEXT, "Log in")
login.click()



