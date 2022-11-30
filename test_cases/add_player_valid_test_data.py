import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player_page import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):
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
        dashboard_page.click_on_the_add_player()
        add_player = AddPlayer(self.driver)
        add_player.title_of_box()
        add_player.type_in_name('Native')
        add_player.type_in_surname('Land')
        add_player.type_in_age('03.05.1992')
        add_player.type_in_main_position('1')
        add_player.click_on_the_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()


