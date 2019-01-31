import unittest

from pageobjects.postscreen import PostScreen
from pageobjects.sidebar import SideBar
from webdriver import Driver
from values import config
from pageobjects.homescreen import HomeScreen
from pageobjects.aboutscreen import AboutScreen
from pageobjects.searchscreen import SearchScreen
import allure

class TestQABoy(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(config.base_url)
        self.driver.instance.maximize_window()

    @allure.story('Story# 1')
    @allure.testcase("Test1")
    def test_home_screen_components(self):
       home_screen = HomeScreen(self.driver)
       home_screen.validate_title_is_present()
       home_screen.validate_icon_is_present()
       home_screen.validate_menu_options_are_present()
       home_screen.validate_posts_are_visible()
       home_screen.validate_social_media_links()
    #
    @allure.testcase("Test2")
    def test_about_screen_components(self):
       home_screen = HomeScreen(self.driver)
       home_screen.click_about_me_link()

       about_screen = AboutScreen(self.driver)
       about_screen.validate_title_is_present()
       about_screen.validate_icon_is_present()
       about_screen.validate_menu_options_are_present()
       about_screen.validate_social_media_links()
       about_screen.validate_about_me_header()
       about_screen.validate_about_me_post()

    @allure.testcase("Test3")
    def test_post_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.click_first_post()

        post_screen = PostScreen(self.driver)
        post_screen.validate_title_is_present()
        post_screen.validate_icon_is_present()
        post_screen.validate_menu_options_are_present()
        post_screen.validate_social_media_links()
        post_screen.validate_featured_image()
        post_screen.validate_published_date()
        post_screen.validate_share_buttons()
        post_screen.validate_comment_section()

    @allure.testcase("Test4")
    def test_search_for_article(self):
        sidebar = SideBar(self.driver)
        sidebar.search_for_article(config.article_title)

        search_screen = SearchScreen(self.driver)
        search_screen.click_article(config.article_title)

        post_screen = PostScreen(self.driver)
        post_screen.validate_article_title(config.article_title)

    @allure.testcase("Test5")
    def test_check_user_comment(self):
        sidebar = SideBar(self.driver)
        sidebar.click_user_comment()

        post_screen = PostScreen(self.driver)
        post_screen.validate_comment_section()

    # @allure.testcase("Test6")
    # def test_archived_articles(self):
    #     sidebar = SideBar(self.driver)
    #     sidebar.click_archive()

    @allure.testcase("Test7")
    def test_article_categories(self):
        sidebar = SideBar(self.driver)
        sidebar.click_category()

    def tearDown(self):
        self.driver.instance.close()
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()