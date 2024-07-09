from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


# driver.get("https://www.speedtest.net/")

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0


    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()