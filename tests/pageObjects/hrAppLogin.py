# this file contains - Page class, Page Locators, Page Actions, WebDriver Init, Custom Functions
# No Assertions in the page class

from selenium.webdriver.common.by import By


class hrAppLogin():

    def __init__(self, driver):
        self.driver = driver

    # Page Locators
    username = (By.XPATH, "//input[@placeholder='Username']")
    password = (By.XPATH, "//input[@name='password']")
    login_btn = (By.XPATH, "//button[@type='submit']")
    error_msg = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def get_username(self):
        return self.driver.find_element(*hrAppLogin.username)

    def get_password(self):
        return self.driver.find_element(*hrAppLogin.password)

    def get_submit_btn(self):
        return self.driver.find_element(*hrAppLogin.login_btn)

    def get_error_message(self):
        return self.driver.find_element(*hrAppLogin.error_msg)

    # Page Actions

    def login_to_hr_App_Login(self, user, pswd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pswd)
        self.get_submit_btn().click()

        # def click_freeTrail(self):
        #     self.get_free_trail_btn().click()

    def get_error_message_text(self):
        return self.get_error_message().text
