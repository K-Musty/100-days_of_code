# Instagram Follower Bot🤖 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.key import Key
import time

INSTA_UNAME = ""
INSTA_PASSWORD = ""
url = "https//:www.instagram.com"

service_path = Service("/usr/local/bin/chromedriver")


class InstaFollower:

    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)

    def login():
        pass

    def find_followers():
        pass

    def follow():
        pass

bot = InstaBot(service=service_path)
bot.login()
bot.find_followers()
bot.follow()
