from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from pathlib import Path
import time


class Bot:
    driver = ""

    def createBot(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features")
        self.driver = webdriver.Chrome(
            Path("C:/Users/User/OneDrive/Desktop/python/Mirea_Bot_2.0/chromedriver/chromedriver.exe"),
            options=options)

    def goto(self, url):
        if not self.checkBrowserOpen(url):
            self.createBot()
            self.testgoto(url)

    def testgoto(self, url):
        self.driver.get(self.checkUrl(url))

    def checkBrowserOpen(self, url):
        try:
            self.driver.get(self.checkUrl(url))
            return True
        except Exception as ex:
            print("Browser is closed: ", ex)
            return False

    def checkUrl(self, url):
        if "https://" in url:
            return url
        else:
            return "https://" + url

    def test_shit(self, btn, closebtn):
        btn2 = self.driver.find_element_by_xpath(btn)
        time.sleep(1)
        btn2.click()
        time.sleep(2)
        print(btn)
        closebtn1 = self.driver.find_element_by_class_name(closebtn)
        time.sleep(0.3)
        closebtn1.click()
        print(closebtn)

    def check(self):
        print("скрипт работает")
        # / html / body / div[3] / div / div / div[3] / button
        # / html / body / div[3] / div / div / div[3] / button / span
        try:  # Сработало
            self.test_shit("/html/body/div[5]/div/div/div[3]/button", "btn-link__text")

        except Exception as ex:
            pass

        try:
            self.test_shit("/html/body/div[3]/div/div/div[3]/button", "/html/body/div[3]/div/div/div[2]/button")

        except Exception as ex:
            pass

        try:
            self.test_shit("btn btn_success btn_material", "btn-link__text")

        except Exception as ex:
            pass
