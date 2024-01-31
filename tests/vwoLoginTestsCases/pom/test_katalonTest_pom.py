import time

import allure
import pytest
from selenium import webdriver

from tests.pageObjects.katalonLoginPage import KatalonloginPage


class TestLogin():
    @allure.epic("Katalon Home Page")
    @allure.feature("TC#0 - Katalon Home page Test")
    @pytest.mark.usefixtures("setup")
    def test_katalon_login(self, setup):
        driver = setup
        driver.get(self.katalon_url)
        katalon_home_page = KatalonloginPage(driver)
        katalon_home_page.click_to_katalon_homePage()
        assert "profile.php#login" in driver.current_url
        time.sleep(2)


    # @allure.epic("VWO Login Test")
    # @allure.feature("TC#1 - VWO App Positive Test")
    # @pytest.mark.usefixtures("setup")
    # def test_vwo_login_positive(self, setup):
    #     driver = setup
    #     driver.get(self.base_url)
    #     login_page = loginPage(driver)
    #     login_page.login_to_vwo(user=self.name, pswd=self.pswd)
    #     time.sleep(5)
    #     assert "Dashboard" in driver.title
    #     time.sleep(5)
