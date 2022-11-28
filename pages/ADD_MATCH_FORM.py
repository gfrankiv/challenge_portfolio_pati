from pages.base_page import BasePage


class AddaMatchForm(BasePage):
    adding_match_player_title_xpath = "//span [text()='Adding match player ala abc']"
    my_team_label_xpath = "//label[text()='My team']"
    my_team_fill_box_xpath = "//input[starts-with(@name, 'myTeam')]"
    submit_button_xpath = "//span[text()='Submit']"
    clear_button_xpath = "//span[text()='Clear']"
    match_at_home_radio_button_xpath = "//input[@name='matchAtHome' and @value='true']"
    match_out_of_home_radio_button_xpath = "//input[@name='matchAtHome' and @value='false']"
    reports_menu_button_xpath = "//span[text()='Reports']"
    date_input_box_xpath = "//input[@aria-invalid='true' and @name='date']"
    general_input_box_xpath = "//input[starts-with(@name,'general')]"
    pass