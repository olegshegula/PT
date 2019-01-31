
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageobjects.basepage import BasePage
import allure
from values import config

class PostScreen(BasePage):
    def __init__(self, driver):
        self.driver = driver

        self.featured_image = WebDriverWait(self.driver.instance, config.wait_timeout).until(
        EC.visibility_of_element_located((
            By.XPATH, "//div/img[@class='attachment-post-thumbnail size-post-thumbnail wp-post-image']")))
        self.published_date = WebDriverWait(self.driver.instance, config.wait_timeout).until(
        EC.visibility_of_element_located((
            By.CSS_SELECTOR, ".entry-date.published")))
        self.share_buttons_container = WebDriverWait(self.driver.instance, config.wait_timeout).until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, "the_champ_sharing_container")))

        self.comment_form = WebDriverWait(self.driver.instance, config.wait_timeout).until(
        EC.visibility_of_element_located((
            By.ID, "commentform")))


    @allure.step("Validate post featured image")
    def validate_featured_image(self):
        assert self.featured_image.is_displayed()


    @allure.step("Validate post published date")
    def validate_published_date(self):
        assert self.published_date.is_displayed()


    @allure.step("Validate post share buttons")
    def validate_share_buttons(self):
        assert self.share_buttons_container.is_displayed()


    @allure.step("Validate post Comment section")
    def validate_comment_section(self):
        assert self.comment_form.is_displayed()

    @allure.step("Validate article title")
    def validate_article_title(self, article_title):
        pass