from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Abdulrahman Kalli")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Mustapha")
email = driver.find_element(By.NAME, value="email")
email.send_keys("kmustapha9564@gmail.com")

button = driver.find_element(By.CSS_SELECTOR, value=".btn ")
button.send_keys(Keys.ENTER)


input("Press Enter to close the browser>>>>> ")