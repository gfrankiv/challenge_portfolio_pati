from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_label_xpath = "// h6[text() = 'Scouts Panel']"
    main_page_menu_button_xpath = "//span[text()='Main page']"
    players_menu_button_xpath = "// span[text() = 'Players']"
    language_button_xpath = "//span[text()='Polski']"
    sign_out_button_xpath = "//span[text()='Sign out']"
    players_count_label_xpath = "//div[text()='Players count']"
    logo_scouts_panel_xpath = "//div[contains(@title, 'Logo Scouts Panel')]"
    add_player_xpath = "//span[text()= 'Add player']"
    dev_team_contact_button_xpath = "//span[text()= 'Dev team contact']"
    activity_bar_xpath = "//h2[text()='Activity']"
    players_count_number_xpath = "//b[text()='789']"
    shortcuts_bar_xpath = "//h2[text()='Shortcuts']"
    matches_count_bar_xpath = "//div[text()='Matches count']"
    reports_count_bar_xpath = "//div[text()='Reports count']"
    events_count_bar_xpath = "//div[text()='Events count']"
    expected_title = 'Scouts panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    add_player_button_xpath = "//*[text()='Add player']"
    players_button_xpath = "//*[text() = 'Players']"
    search_field_xpath = "//*[@aria-label = 'search']"

    def click_on_the_add_player(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        pass

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def type_in_search_field(self, search_field):
        self.field_send_keys(self.search_field_xpath, search_field)

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.SendKeys = 'Enter'

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)
