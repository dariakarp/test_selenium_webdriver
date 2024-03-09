import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_open_page(driver):
    driver.get("http://localhost/litecart/en/")
    products = driver.find_elements("xpath","//div[@class='image-wrapper']")
    for i in range(len(products)):
        products = driver.find_elements("xpath", "//div[@class='image-wrapper']")
        product = products[i]
        sticker = product.find_element("xpath", "//*[contains(@class, 'sticker')]")
        assert len(sticker) == 1




