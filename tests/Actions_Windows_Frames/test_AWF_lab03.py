import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_actions_03():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    click_input_box = driver.find_element(By.XPATH, "//input[@id='clickable']")
    actions = ActionChains(driver)
    actions.click_and_hold(click_input_box).key_down(Keys.SHIFT).send_keys("dileep").key_up(Keys.SHIFT).perform()
    # actions.click_and_hold(click_input_box).key_down(Keys.SHIFT).key_down("dileep").perform()

    click_anchor_tag = driver.find_element(By.XPATH,"//a[@id='click']")
    ActionChains(driver).click(click_anchor_tag).perform()

    assert "resultPage.html" in driver.current_url


    time.sleep(15)
