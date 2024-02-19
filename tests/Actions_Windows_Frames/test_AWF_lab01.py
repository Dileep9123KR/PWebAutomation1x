import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_actions_01():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    # Need to create the Action Chains Class
    actions = ActionChains(driver)
    # Here we need send keys with CAPS lock
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "dileep").key_up(Keys.SHIFT).perform()

    last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
    # actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(last_name, "raveendran").key_up(Keys.SHIFT).perform()
    # time.sleep(10)

    # url = driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Download File']")
    # actions.context_click(url).perform()

    driver.get("https://awesomeqa.com/selenium/single_text_input.html")
    actions.send_keys("Selenium")

    time.sleep(15)
