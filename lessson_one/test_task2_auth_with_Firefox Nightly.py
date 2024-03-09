#открытие приложения через браузер Firefox Nightly

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

firefox_options = Options()
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = "C:\\Program Files\\Firefox Nightly\\firefox.exe"


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(firefox_options)
    request.addfinalizer(wd.quit)
    return wd

def test_open_page(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()
    time.sleep(20)

