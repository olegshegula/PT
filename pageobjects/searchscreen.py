from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from pageobjects.basepage import BasePage

class SearchScreen(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.page_header = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//h1[contains(text(), 'Search Results')]")))
        self.article_title = None

    @allure.step("Click an article")
    def click_article(self, article_title):
        self.article_title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.LINK_TEXT, article_title)))
        self.article_title.click()