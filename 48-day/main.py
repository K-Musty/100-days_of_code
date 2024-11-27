from selenium import webdriver
from selenium.webdriver.chrome.service import Service



service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

price = driver.find_element(id, "priceblock_ourprice")
print(price.text)

# driver.close()
driver.quit()