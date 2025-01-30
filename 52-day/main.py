# Instagram Follower Bot🤖
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

INSTA_UNAME = ""
INSTA_PASSWORD = ""
url = "https://www.instagram.com/accounts/login/"
TARGET_ACCOUNT = "ChefSteps"

service_path = Service("/usr/local/bin/chromedriver")


class InstaFollower:

    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get(url=url)
        time.sleep(5)

        username = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[1]/div/label/input")
        username.send_keys(INSTA_UNAME)
        password_field = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[2]/div/label/input")
        password_field.send_keys(INSTA_PASSWORD)

        time.sleep(3)
        password_field.send_keys(Keys.ENTER)


    def find_followers(self):
        self.driver.get(url=f"https://www.instagram.com/{TARGET_ACCOUNT}/followers/")
        time.sleep(5)
        # Scrolling feature

    def follow(self):
        self.driver.find_elements(By.XPATH, "")
        time.sleep(5)
        pass

bot = InstaFollower(service=service_path)
bot.login()
bot.find_followers()
bot.follow()
