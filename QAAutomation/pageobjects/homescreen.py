from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pageobjects.basepage import BasePage
from values import config

class HomeScreen(BasePage):

    def __init__(self,driver):
        self.driver = driver

        self.post_list = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_all_elements_located((
                By.TAG_NAME, "article")))
    def validate_posts_are_visible(self):
        assert len(self.post_list) > 0

    def click_about_me_link(self):
       about_me_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[text()='About Me'][1]")))
       about_me_link.click()
        # time.sleep(10)

       def click_first_post(self):
        self.first_post = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//article[1]//h3/a")))
        self.first_post.click()





