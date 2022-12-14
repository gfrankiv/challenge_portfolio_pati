from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_button_xpath = "//*[text()='Add player']"
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name = 'name']"
    surname_field_xpath = "//*[@name='surname']"
    phone_field_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@name='weight']"
    height_field_xpath = "//*[@name='height']"
    age_field_xpath = "//*[@type='date']"
    leg_select_button_xpath = "//*[@role='button' and @id='mui-component-select-leg']"
    club_field_xpath = "//*[@name='club']"
    main_position_xpath = "//*[ @ name = 'mainPosition']"
    district_button_xpath = "//*[@role ='button' and @id='mui-component-select-district']"
    submit_button_xpath = "//*[text()='Submit']"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    title_of_box_xpath = "//form/descendant::div/div/span[1]"
    players_button_xpath = "//*[text() = 'Players']"

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_box(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

