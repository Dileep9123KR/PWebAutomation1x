import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_actions_02():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions = ActionChains(driver)
    actions.send_keys("Selenium")

    time.sleep(15)
