import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd
def test_logi_browser_in_page(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()

    driver.get(" http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    time.sleep(2)
    products = driver.find_elements("xpath", "//tr[@class='row'][position()>3]/td[3]/a")
    for i in range(len(products)):
        products = driver.find_elements("xpath", "//tr[@class='row'][position()>3]/td[3]/a")
        product = products[i]
        product.click()
        for j in driver.get_log("browser"): #проверка сообщений в логах браузера
            print(j)
        driver.back()