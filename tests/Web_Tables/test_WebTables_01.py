import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# STATIC TABLE
def test_web_tables():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")

    # next step is to find how many rows and columns in the table
    # Xpath - //table[@id='customers'] - for whole table
    # Xpath - //table[contains(@id,'custo')]//tbody/tr -> for all table rows
    # Xpath - //table[contains(@id,'custo')]//tbody/tr[2]/td -for columns

    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'custo')]//tbody/tr")
    row = len(row_elements)
    print(row)

    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'custo')]//tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    # select table contents- Iwant to select compamy "Adobe" and contact as "Yoshi Tannamuri"
    # So the Xpath will be - //table[contains(@id,'custo')]//tbody/tr[6]/td[2]
    # sometimes tr[](2-7) and td[](1-3) will be dynamic in nature

    first_part = "//table[contains(@id,'custo')]//tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            # print(dynamic_path)
            # print(driver.find_element(By.XPATH,dynamic_path).text)
            data = driver.find_element(By.XPATH, dynamic_path).text  # Interview ques; find Helen Bennett's country?
            # Xpath - //table[contains(@id,'custo')]//tbody/tr[5]/td[2]/following-sibling::td
            if "Helen Bennett" in data:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennet is in {country_text}")

            # print(data.text, end=" ")

    time.sleep(5)
    driver.quit()
