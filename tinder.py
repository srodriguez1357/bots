from selenium import webdriver
from time import sleep
from pynput.keyboard import Key, Controller
from random import randint

keyboard = Controller()

path = r"C:\Users\Salvador\Downloads\chromedrive\chromedriver.exe"

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(path)

    def proceso(self):
        self.driver.get('https://tinder.com')

        sleep(7)

        facebuttn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        facebuttn.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('chemsapeluchadito@gmail.com')

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('Yo123456789')

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)

        sleep(7)

        popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup1.click()

        popup2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup2.click()

        acep = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        acep.click()

        sleep(3)
        i = 0
        while True:
            choice = randint(1, 10)
            if choice > 5:
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                i = i + 1
                print(i)

            else:
                keyboard.press(Key.up)
                keyboard.release(Key.up)
                keyboard.press(Key.down)
                keyboard.release(Key.down)
                keyboard.press(Key.left)
                keyboard.release(Key.left)
            sleep(1.3)

       # like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        #like_btn.click()
 #   def like(self):

    #def dislike(self):
     #   dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
      #  dislike_btn.click()

    #def auto_swipe(self):
     #   while True:
      #      sleep(5)
       #     self.like()
       #     except Exception:
        #        try:
         #           self.close_popup()
          #      except Exception:
           #         self.close_match()

   # def close_popup(self):
    #    popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
     #   popup_3.click()

    #def close_match(self):
     #   match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
      #  match_popup.click()

bot = TinderBot()
bot.proceso()
