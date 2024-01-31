# this file contains - Page class, Page Locators, Page Actions, WebDriver Init, Custom Functions
# No Assertions in the page class

from selenium.webdriver.common.by import By


class KatalonloginPage():

    def __init__(self,driver):
        self.driver = driver

    #Page Locators
    make_appointment_btn = (By.XPATH, "//a[@id='btn-make-appointment']")

    def get_make_appointment(self):
        return self.driver.find_element(*KatalonloginPage.make_appointment_btn)


    #Page Actions

    def click_to_katalon_homePage(self):
        self.get_make_appointment().click()

