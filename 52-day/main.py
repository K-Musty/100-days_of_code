# Instagram Follower Bot🤖 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.key import Key

INSTA_UNAME = ""
INSTA_PASSWORD = ""

service = Service("/usr/local/bin/chromedriver")

driver = webdriver.chrome(service=service)
driver.findelement()

driver.quit()
