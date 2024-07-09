import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 350
PROMISED_UP = 350
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_USER = os.environ["TWITTER_USER"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

TEST_DOWN_XPATH = ('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                   '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
TEST_UP_XPATH = ('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                 'div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

TWEET_FIELD_XPATH = ('//*[@id="react-root"]/div/div/div[2]/main/'
                     'div/div/div/div/div/div[3]/div/div[2]/div[1]/'
                     'div/div/div/div[2]/div[1]/div/div/div/div/div/'
                     'div/div/div/div/div/div/div[1]/div/div/div/div/'
                     'div/div/div')

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
        self.driver.get("https://x.com/login")

        # Email Field
        time.sleep(2)
        email = self.driver.find_element(By.CLASS_NAME, value="r-30o5oe")
        email.send_keys(TWITTER_USER)
        email.send_keys(Keys.ENTER)
        time.sleep(5)

        # Password Field
        time.sleep(3)
        # Try loop to catch verification w email
        try:
            password = self.driver.find_element(By.NAME, value="password")

        except NoSuchElementException:
            verify_field = self.driver.find_element(By.CLASS_NAME, value="r-30o5oe")
            verify_field.send_keys(TWITTER_EMAIL)
            verify_field.send_keys(Keys.ENTER)
            time.sleep(3)

            password = self.driver.find_element(By.NAME, value="password")
            time.sleep(2)

        finally:
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)

            time.sleep(7)


        # Draft Tweet
        tweet_field = self.driver.find_element(By.CLASS_NAME, value="public-DraftEditor-content")
        time.sleep(1)
        # tweet_field.click()
        # tweet_field.send_keys(f"Hey ATT, why is my internet speed {self.down} down/ "
        #                       f"{self.up} up when I pay for {PROMISED_DOWN} down/ {PROMISED_UP} up?")
        # post_text = self.driver.find_element(By.XPATH, value=TWEET_FIELD_XPATH)
        tweet_field.send_keys("Hey ATT, why is my internet speed 50down/5up?")




bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()