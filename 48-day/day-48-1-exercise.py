from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

