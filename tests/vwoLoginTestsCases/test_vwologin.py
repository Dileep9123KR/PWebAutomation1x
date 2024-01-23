# It contains Assertions
import time

import pytest
import allure
from tests.pageObjects.loginPage import loginPage
from tests.pageObjects.dashboardPage import dashboardPage
from selenium.webdriver.common.by import By
from selenium import webdriver
#from dotnet import load_dotenv

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    return driver


@allure.epic("VWO Login Test")
@allure.feature("TC#1 - VWO App Positive Test")
def test_vwo_login(setup):
    driver = setup
    login_page = loginPage(driver)
    login_page.login_to_vwo(user="contact+atb5x@thetestingacademy.com",pswd="ATBx@1234")
    time.sleep(5)
    assert "Dashboard" in driver.title
    time.sleep(5)


def tear_down(): # for closing window(browser tab)
    pass