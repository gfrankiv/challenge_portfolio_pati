from pages.base_page import BasePage
#
#
class LoginPage(BasePage):
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//*[@id='password']"
     sign_in_button_xpath = "//[text()='Sign in']"
     scouts_panel_label_xpath = "//*[text()= 'Scouts Panel']"
     english_button_xpath = "//div[@aria-haspopup= 'listbox' or @role= 'button']"
     remind_password_xpath = "//a[text()='Remind password']"
     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)
