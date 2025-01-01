from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10

service = Service("usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)
# Twitter (X) Login
X_EMAIL = ""
X_PASSWORD = ""
driver.get("https://www.x.com")


class InternetSpeedTwitterBot:

    def __init__(self, down, up):
        self.down = down
        self.up = up


    def get_internet_speed(self):
        pass


    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(up=PROMISED_UP, down=PROMISED_DOWN)
internet_speed = bot.get_internet_speed()
tweet_at = bot.tweet_at_provider()