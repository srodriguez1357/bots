from selenium import webdriver
from time import sleep

path = r"C:\Users\Salvador\Downloads\chromedrive\chromedriver.exe"

class Counterbot:
    def __init__(self):
        self.driver = webdriver.Chrome(path)

    def search(self):
        self.driver.get('https://scorecounter.com/click-counter/')
        sleep(1)

    def close(self):
        close = self.driver.find_element_by_xpath('//*[@id="closeSettings"]')
        close.click()

    def clickily(self):
        butt = self.driver.find_element_by_xpath('//*[@id="counter1"]/div[3]')
        butt.click()
        sleep(.7)

bot = Counterbot()

bot.search()
bot.close()
while True:
    bot.clickily()
