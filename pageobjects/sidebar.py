from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from values import config

class SideBar():
    def __init__(self, driver):
        self.driver = driver

        self.search_bar = WebDriverWait(self.driver.instance, config.wait_timeout).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "search-field")))
        self.search_submit = WebDriverWait(self.driver.instance, config.wait_timeout).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "search-submit")))
        self.user_comment = WebDriverWait(self.driver.instance, config.wait_timeout).until(
            EC.visibility_of_element_located((
                By.XPATH, "//li[@class='recentcomments'][1]/a")))
        # self.archive_link = WebDriverWait(self.driver.instance, config.wait_timeout).until(
        #     EC.visibility_of_element_located((
        #         By.XPATH, "//section[@id='archives-2']//li[1]/a")))
        self.category_link = WebDriverWait(self.driver.instance, config.wait_timeout).until(
            EC.visibility_of_element_located((
                By.XPATH, "//section[@id='categories-4']//li[1]/a")))

    @allure.step("Search for an Article")
    def search_for_article(self, article_title):
        self.search_bar.send_keys(article_title)
        self.search_submit.click()

    @allure.step("Click user comment")
    def click_user_comment(self):
        self.user_comment.click()

    @allure.step("Click archive")
    def click_archive(self):
        self.archive_link.click()

    @allure.step("Click category")
    def click_category(self):
        self.category_link.click()