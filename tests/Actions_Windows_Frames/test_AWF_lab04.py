import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_actions_04():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #driver.find_element(By.XPATH,"//a[@id='click']").click()
    driver.find_element(By.ID,"click").click()

    actions_builder = ActionBuilder(driver)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.pointer_action.pointer_down(MouseButton.BACK)
    actions_builder.perform()



    
    time.sleep(20)
