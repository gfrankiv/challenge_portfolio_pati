from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class LoginPage(BasePage):
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//*[@id='password']"
     sign_in_button_xpath = "//*[text()='Sign in']"
     login_url = ('https://scouts-test.futbolkolektyw.pl/en')
     expected_title = 'Scouts panel - sign in'
     label_xpath = "//*[text()= 'Scouts Panel']"
     english_button_xpath = "//div[@aria-haspopup= 'listbox' or @role= 'button']"
     remind_password_xpath = "//a[text()='Remind password']"
     type_in_email_xpath = "//*[@value= 'user03@getnada.com']"
     title_of_box_xpath = "//*[@id = '__next']/form/div/div[1]/h5"



     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)
     def type_in_password(self, password):
         self.field_send_keys(self.password_field_xpath, password)
     def click_on_the_sign_in_button(self):
         self.click_on_the_element(self.sign_in_button_xpath)
     def title_of_page(self):
         assert self.get_page_title(self.login_url) == self.expected_title










