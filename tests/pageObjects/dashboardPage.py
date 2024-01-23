# Page Locators and Page Actions

from selenium.webdriver.common.by import By

class dashboardPage():

    def __int__(self, driver):
        self.driver = driver

    user_logged_in = (By.XPATH,"//span[@data-qa='lufexuloga']")


    def get_logged_username(self):
        return self.driver.find_element(*dashboardPage.user_logged_in)

    def userLoggedIn_text(self):
        return self.get_logged_username().text()