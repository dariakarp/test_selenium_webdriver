import time

import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_registr_new_user(driver):
    driver.get("http://localhost/litecart/")
    link_create_account = driver.find_element("xpath", "//form[@name = 'login_form']//a")
    link_create_account.click()
    driver.find_element("name", "firstname").send_keys("Тюльпанна")
    driver.find_element("name", "lastname").send_keys("Сергеевна")
    driver.find_element("name", "address1").send_keys("Спортивная, 18")
    driver.find_element("name", "postcode").send_keys("98989")
    driver.find_element("name", "city").send_keys("Лучший")
    driver.find_element("id", "select2-country_code-ja-container").click()
    time.sleep(2)