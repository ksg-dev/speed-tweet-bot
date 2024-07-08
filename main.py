from selenium import webdriver
from selenium.webdriver.common.by import By
# Use this class to use specific keys besides letters/numb
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Open speedtest window
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.speedtest.net/")

