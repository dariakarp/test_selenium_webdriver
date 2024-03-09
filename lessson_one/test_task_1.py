import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd

def test_open_page(driver):
    driver.get("https://www.google.com/")
    driver.find_element("name", "q").send_keys("Hello, world!")
    time.sleep(3)
    driver.find_element("name", "btnK").click()
    time.sleep(5)