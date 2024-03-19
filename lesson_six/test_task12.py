import time

import pytest
import os
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from faker import Faker
fake = Faker()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_registr_new_user(driver): #регистрация пользователя
    driver.get("http://localhost/litecart/admin") #регистрация пользователя
    driver.find_element("name", "username").send_keys("admin") #ввод логина
    driver.find_element("name", "password").send_keys("admin") #ввод пароля
    driver.find_element("name", "login").click()

    driver.find_element("xpath", "//ul[@id = 'box-apps-menu']//li[2]").click() #клик на пункт меню Каталог

    name = fake.name()
    driver.find_element("xpath", "//a[@class = 'button'][2]/i").click() #клик на кнопку AddNewProduct
    driver.find_element("xpath", "//input[@name = 'name[en]']").send_keys(name)
    driver.find_element("xpath", "//input[@name = 'code']").send_keys("999")
    driver.find_element("xpath", "//div[@id = 'tab-general']//tr[7]//tr[2]/td").click()

    relative_path = "mqdefault.jpg"
    current_dir = os.path.dirname(os.path.abspath("mqdefault.jpg"))
    absolute_path = os.path.join(current_dir, relative_path).replace("\\", "/")

    driver.find_element("xpath", "//input[@name = 'new_images[]']").send_keys(absolute_path)
    driver.find_element("xpath", "//input[@name = 'date_valid_from']").send_keys("19/03/2024")
    driver.find_element("xpath", "//input[@name = 'date_valid_to']").send_keys("30/03/2024")

    driver.find_element("xpath", "//ul[@class = 'index']/li[2]").click() #клик на вкладку information
    time.sleep(3)

    driver.find_element("xpath", "//select[@name = 'manufacturer_id']").click()
    driver.find_element("xpath", "// select[ @ name = 'manufacturer_id'] / option[ @ value = '1']").click()
    driver.find_element("xpath", "//div[@class = 'trumbowyg-editor' ]").send_keys("зеленая лягушка")

    driver.find_element("xpath", "//ul[@class = 'index']/li[4]").click()  # клик на вкладку data
    time.sleep(3)

    driver.find_element("xpath", "//input[@name = 'purchase_price']").clear()
    driver.find_element("xpath", "//input[@name = 'purchase_price']").send_keys("5")
    driver.find_element("xpath", "//select[@name = 'purchase_price_currency_code']").click()
    driver.find_element("xpath", "//select[@name = 'purchase_price_currency_code']/option[@value = 'EUR']").click()

    driver.find_element("xpath", "//input[@name = 'prices[USD]']").send_keys("2")
    driver.find_element("xpath", "//input[@name = 'prices[EUR]']").send_keys("3")
    driver.find_element("xpath", "// button[ @ name = 'save']").click() #сохраняю товар

    driver.find_element("xpath", "//li[@id = 'doc-catalog']/a").click() #клик на пункт меню "каталог"
    driver.find_element("xpath", "//input[@type = 'search']").send_keys(name) #ввод названия созданного товара в поле поиска
    driver.find_element("xpath", "//input[@type = 'search']").send_keys(Keys.ENTER)

    product = driver.find_element("xpath", "//tr[@class = 'row semi-transparent']").text
    assert product == name









