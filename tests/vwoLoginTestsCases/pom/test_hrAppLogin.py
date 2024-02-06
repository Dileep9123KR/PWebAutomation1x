import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from tests.pageObjects.hrAppLogin import hrAppLogin


class TestLogin():
    @allure.epic("HR Module Test")
    @allure.feature("TC#0 - HR App Negative Test")
    @pytest.mark.usefixtures("setup")
    def test_hrApp_login_negative(self, setup):
        driver = setup
        driver.get(self.hr_url)
        login_page = hrAppLogin(driver)
        time.sleep(5)
        login_page.login_to_hr_App_Login(user="admin", pswd="admin")
        time.sleep(10)
        error_msg = login_page.get_error_message_text()
        assert error_msg == "Invalid credentials"
        time.sleep(5)

    # @allure.epic("HR Module Test")
    # @allure.feature("TC#1 - HR App Positive Test")
    # @pytest.mark.usefixtures("setup")
    # def test_vwo_login_positive(self, setup):
    #     driver = setup
    #     driver.get(self.hr_url)
    #     login_page = hrAppLogin(driver)
    #     login_page.login_to_hr_App_Login(user=self.name, pswd=self.pswd)
    #     time.sleep(5)
    #     assert "Dashboard" in driver.title
    #     time.sleep(5)
