import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 150
PROMISED_UP = 10

service_path = Service("/usr/local/bin/chromedriver")

# Twitter (X) Login
X_EMAIL = ""
X_USERNAME = "montana70463"
X_PASSWORD = ""


class InternetSpeedTwitterBot:

    def __init__(self, service):
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        accept_button = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        accept_button.click()

        time.sleep(5)
        start = self.driver.find_element(By.CLASS_NAME, "class-text")
        start.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.up = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        return self.down, self.up


    def tweet_at_provider(self):
        self.driver.get("https://www.x.com")

        login_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div/span/span")
        login_button.click()

        input_email = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        input_email.send_keys(X_EMAIL)
        input_email.send_keys(Keys.ENTER)

        input_username = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        input_username.send_keys(X_USERNAME)


        # Password
        input_password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        input_password.send_keys(X_PASSWORD)
        input_password.send_keys(Keys.ENTER)

        # Post
        click_post = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div")
        click_post.click()

        time.sleep(5)
        post_compose = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        post_compose.send_keys(tweet)

        time.sleep(3)

        post_button = self.driver.find_element(By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]")
        post_button.click()

        time.sleep(2)
        return f"pass"


bot = InternetSpeedTwitterBot(service=service_path)
internet_speed = bot.get_internet_speed()
tweet_at = bot.tweet_at_provider()
