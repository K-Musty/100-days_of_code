from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

MY_EMAIL = ""
MY_PASSWORD = ""



url = "https://www.linkedin.com/jobs/search/?currentJobId=4071837289&geoId=103535056&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true"



service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)



driver.get(url)

