import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestCheckSearchPlayer(unittest.TestCase):
    s = Service(DRIVER_PATH)
    driver = None

    os.chmod(DRIVER_PATH, 755)

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user04@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        time.sleep(5)
        dashboard_page.click_on_the_players_button()
        dashboard_page.type_in_search_field('Native')
        time.sleep(5)

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.SendKeys = 'Enter'

    @classmethod
    def tearDown(self):
        self.driver.quit()
