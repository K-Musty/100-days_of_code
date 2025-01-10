from selenium import webdriver
from selenium.webdriver.service import Service
from selenium.webdriver.by import By

url = ""

service = Service(url)

driver = webdriver.chrome(service=service)
