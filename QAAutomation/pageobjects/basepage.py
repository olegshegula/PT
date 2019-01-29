from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from values import config

class BasePage:
    def validate_title_is_present(self):
        self.title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "site-title")))
        assert self.title.is_displayed()

    def validate_icon_is_present(self):
        self.icon = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "custom-logo")))
        assert self.icon.is_displayed()

    def validate_menu_options_are_present(self):
        self.top_menu = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "primary-menu")))
        assert self.top_menu.is_displayed()

    def validate_social_media_links(self):
        self.twitter_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//span[contains(text(), 'Twitter')]")))

        self.linkedin_button = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//span[contains(text(), 'LinkedIn')]")))

        assert self.twitter_button.is_displayed()
        assert self.linkedin_button.is_displayed()