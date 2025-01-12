# Instagram Follower Bot🤖 
from selenium import webdriver
from selenium.webdriver.service import Service
from selenium.webdriver.by import By
from selenium.webdriver.common.key import Key

INSTA_UNAME = ""
INSTA_PASSWORD = ""

url = ""

service = Service(url)

driver = webdriver.chrome(service=service)
driver.quit()
