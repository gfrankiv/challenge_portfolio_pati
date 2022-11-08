# **Task 1: Software configuration.**

##  *“Subtask 1: Why did I choose to participate in the Dare IT Challenge?”*

  Hi! My name is Halyna. I choose to participate in the Dare IT Challenge, as it is a great chance to prove my skills and to learn the automation testing. This challenge motivates me to move further and to fight for the opportunity to become the intern of one of the best IT companies in Poland.


And, of course, my goal is to win in this marathon and to get the job 😉 


# **"TASK 2: selectors"**

## scouts_panel_hyperlink_xpath

//*[text() = 'Scouts Panel']

//h5[starts-with(@class,"MuiTypography")]

//h5[contains(@class,"MuiTypography-root")] 

## login_hyperlink_xpath

//input[contains(@id, "login")]

//input [@name = "login" and @type = "text"]

//input [@id = "login" or @aria-invalid = "false"]

## password_hyperlink_xpath

//input[@id = "password" or @name = "password"]

//input[contains (@id, "password")]

//input[starts-with(@id, "password")]

## remind_password_hyperlink_xpath

//a[starts-with(@tabindex,"-1")]

//a[text()="Remind password"]

//a[@tabindex="-1" and text()="Remind password"]

## english_polish_hyperlink_xpath

//div[contains(@class, "MuiSelect-root")]

//div[text()="English"]

//div [@aria-haspopup="listbox" or @role="button"]

## sign_in_hyperlink_xpath

//span [text()="Sign in"]

//span [@class="MuiButton-label"]

//span [contains(@class,"MuiButton-label")]