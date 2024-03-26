import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import pytest
import os
from selenium import webdriver
from faker import Faker
fake = Faker()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd


def test_work_in_basket(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/en/")
    product_in_box = 0
    for i in range(3):
        driver.find_elements("xpath", "//li[@class= 'product column shadow hover-light']")
        driver.find_element("xpath", "//div[@class= 'image-wrapper']").click()
        try:
            driver.find_element("xpath", "//select[@name= 'options[Size]']")
            driver.find_element("xpath", "//select[@name= 'options[Size]']").click()
            driver.find_element("xpath", "//select[@name= 'options[Size]']/option[3]").click()
            driver.find_element("xpath", "//button[@name = 'add_cart_product']").click()
        except NoSuchElementException:
            print("нет ошибки")
            driver.find_element("xpath", "//button[@name = 'add_cart_product']").click()

        product_in_box += 1
        count_wait = str(product_in_box)
        wait.until(EC.text_to_be_present_in_element(("xpath", "//div[@id = 'cart']//span[@class = 'quantity']"), count_wait))
        driver.back()
    driver.find_element("xpath", "//div[@id ='cart']/a[3]").click() #клик на "Checkout" на корзину

    buttons_delete = driver.find_elements("xpath", "//form[@name='cart_form']//button[@name = 'remove_cart_item']")  # нахожу кнопки Удалить
    for j in range(len(buttons_delete)):
        table = driver.find_element("xpath", "//div[@id = 'box-checkout-summary']")  # нахожу таблицу по локатору
        button = driver.find_element("xpath", "//form[@name='cart_form']//button[@name = 'remove_cart_item']")
        button.click() #кликаю на кнопку delete
        wait.until(EC.staleness_of(table))  # жду пока талица обновится















