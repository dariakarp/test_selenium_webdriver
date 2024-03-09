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
    driver.get("http://localhost/litecart/admin")
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()

    elements = driver.find_elements("xpath", "//span[@class='fa-stack fa-lg icon-wrapper']")#находит все внешние элементы меню на странице

    for i in range(len(elements)):
        elements = driver.find_elements("xpath", "//span[@class='fa-stack fa-lg icon-wrapper']")
        element = elements[i].click()
        title = driver.find_element("xpath","//h1")


        menu_items = driver.find_elements("xpath", "//ul[@class = 'docs']//span[@class = 'name']")
        for j in range(len(menu_items)):
            menu_items = driver.find_elements("xpath", "//ul[@class = 'docs']//span[@class = 'name']")
            menu_item = menu_items[j].click()
            title = driver.find_element("xpath", "//h1")
            


