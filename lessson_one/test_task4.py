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
        products = driver.find_elements("xpath", "//div[@class='image-wrapper']") #находит все карточки товаров
        product = products[i]#берет i-тый элемент
        sticker = product.find_elements("xpath", ".//*[contains(@class, 'sticker')]") #находит у i-того элемента стикер
        assert (len(sticker)) == 1 #ожидаю, что стикер строго 1




