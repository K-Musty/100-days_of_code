from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10

service = Service("usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)
# Twitter (X) Login
X_EMAIL = ""
X_PASSWORD = ""
driver.get("https://www.x.com")