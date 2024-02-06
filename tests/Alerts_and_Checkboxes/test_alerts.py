from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_alerts_testing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # click_btn_1 = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    # click_btn_1.click()
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.alert_is_present())
    # alert = driver.switch_to.alert
    # alert.accept()
    #
    # result = driver.find_element(By.XPATH, "//p[@id='result']")
    # print(result.text)

    click_btn_3 = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    click_btn_3.click()
    wait =  WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    alert = driver.switch_to.alert
    # alert.dismiss() # for clicking cancel on the alert pop up / for negative test case
    alert.send_keys("Dileep")
    alert.accept()

    result = driver.find_element(By.XPATH, "//p[@id='result']")
    print(result.text)

