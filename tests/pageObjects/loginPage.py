# this file contains - Page class, Page Locators, Page Actions, WebDriver Init, Custom Functions
# No Assertions in the page class

from selenium.webdriver.common.by import By


class loginPage():

    def __init__(self,driver):
        self.driver = driver

    #Page Locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    submit_btn = (By.XPATH,"//button[@id='js-login-btn']")
    #forgot_pswd_btn = (By.XPATH,"//button[normalize-space()='Forgot Password?']")
    error_msg = (By.CSS_SELECTOR,"#js-notification-box-msg")
    # free_trail_btn = (By.XPATH, "//a[normalize-space()='Start a free trail']")
    # sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    # remember_me_chkbox = (By.XPATH, "//label[@for='checkbox-remember']//span[@class='checkbox-radio-button ng-scope']//*[name()='svg']")

    # Need to return the webElements

    def get_username(self):
        return self.driver.find_element(*loginPage.username)

    def get_password(self):
        return self.driver.find_element(*loginPage.password)

    def get_submit_btn(self):
        return self.driver.find_element(*loginPage.submit_btn)

    def get_error_message(self):
        return self.driver.find_element(*loginPage.error_msg)

    # def get_free_trail_btn(self):
    #     return self.driver.find_element(*loginPage.free_trail_btn)



    #Page Actions

    def login_to_vwo(self, user, pswd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pswd)
        self.get_submit_btn().click()


    # def click_freeTrail(self):
    #     self.get_free_trail_btn().click()