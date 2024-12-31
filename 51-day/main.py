from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
driver = webdriver.Service(service=service)