import pytest
from selenium import webdriver
from dotenv import load_dotenv

import os

load_dotenv()
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.get("https://app.vwo.com")

    name = os.getenv("NAME")
    pswd = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    katalon_url = os.getenv("KATALON_URL")
    hr_url = os.getenv("HR_APP_URL")


    request.cls.driver = driver
    request.cls.name = name
    request.cls.pswd = pswd
    request.cls.base_url = base_url
    request.cls.katalon_url = katalon_url
    request.cls.hr_url = hr_url

    yield driver
    driver.quit()
