from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# price = driver.find_element(by="class name", value="a-price-whole")
# print(price.text)

driver.get("https://www.python.org/")
# search_bar = driver.find_element(by="name", value="q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, value="python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

xpath_essay = driver.find_element(By.XPATH, value="/html/body/div/footer/div[1]/div/ul/li[3]/ul/li[9]/a")
print(xpath_essay.text)

# driver.close()
driver.quit()