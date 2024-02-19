import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


def test_actions_05(): 
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.makemytrip.com/')

    time.sleep(5)

    fromCity = driver.find_element(By.XPATH,"//input[@id='fromCity']")
    actions = ActionChains(driver)
    actions.move_to_element(fromCity).click().send_keys("New Delhi").perform()

    time.sleep(20)
