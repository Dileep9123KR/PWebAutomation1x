import time

import allure
import pytest
from selenium import webdriver

from tests.pageObjects.loginPage import loginPage


class TestLogin():
    @allure.epic("VWO Login Test")
    @allure.feature("TC#0 - VWO App Negative Test")
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        login_page = loginPage(driver)
        login_page.login_to_vwo(user="admin", pswd="admin")
        time.sleep(5)
        error_msg = login_page.get_error_message_text()
        assert error_msg == "Your email, password, IP address or location did not match"
        time.sleep(5)

    @allure.epic("VWO Login Test")
    @allure.feature("TC#1 - VWO App Positive Test")
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        login_page = loginPage(driver)
        login_page.login_to_vwo(user=self.name, pswd=self.pswd)
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(5)
