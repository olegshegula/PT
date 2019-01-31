from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.basepage import BasePage
import time
import allure
from values import config

class AboutScreen(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.about_me_header = WebDriverWait(self.driver.instance, config.wait_timeout).until(
        EC.visibility_of_element_located((
            By.XPATH, "//h1[contains(text(), 'About Me')]")))
        self.about_me_post = WebDriverWait(self.driver.instance, config.wait_timeout).until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, "entry-content")))

    @allure.step("Validate about me header")
    def validate_about_me_header(self):
        assert self.about_me_header.is_displayed()

    @allure.step("Validate about me post")
    def validate_about_me_post(self):
        assert self.about_me_post.is_displayed()

