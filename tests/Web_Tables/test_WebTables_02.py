import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# DYNAMIC TABLE
def test_web_tables():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable1.html")
    # Get the table to perform with a dynamic data
    table = driver.find_element(By.XPATH,"//table[@summary='Sample Table']/tbody")
    #table_rows = "//table[@summary='Sample Table']/tbody/tr"
    #or
    table_rows = table.find_elements(By.TAG_NAME,"tr") # this is called find element chaining and it should be within the table

    for row in table_rows:
        cols = row.find_elements(By.TAG_NAME,"td")
        for e in cols:
            print(e.text)


    time.sleep(5)
    driver.quit()
