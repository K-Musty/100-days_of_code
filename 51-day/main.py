from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10

service_path = Service("usr/local/bin/chromedriver")

# Twitter (X) Login
X_EMAIL = ""
X_PASSWORD = ""
# driver.get("https://www.x.com")


class InternetSpeedTwitterBot:

    def __init__(self, service):
        self.service = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        pass


    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(service_path)
internet_speed = bot.get_internet_speed()
tweet_at = bot.tweet_at_provider()