import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 350
PROMISED_UP = 350
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

TEST_DOWN_XPATH = ('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                   '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
TEST_UP_XPATH = ('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                 'div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(2)
        self.up = self.driver.find_element(By.XPATH, value=TEST_UP_XPATH).text
        self.down = self.driver.find_element(By.XPATH, value=TEST_DOWN_XPATH).text
        loading = True

        while loading:
            time.sleep(10)
            self.up = self.driver.find_element(By.XPATH, value=TEST_UP_XPATH).text
            self.down = self.driver.find_element(By.XPATH, value=TEST_DOWN_XPATH).text
            if self.up != "—":
                loading = False

        print(f"down: {self.down}")
        print(f"up: {self.up}")



    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()