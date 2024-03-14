import time

import pytest
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
    driver.get("http://localhost/litecart/")
    email = fake.email()
    link_create_account = driver.find_element("xpath", "//form[@name = 'login_form']//a")
    link_create_account.click()
    driver.find_element("name", "firstname").send_keys("Тюльпанна")
    driver.find_element("name", "lastname").send_keys("Сергеевна")
    driver.find_element("name", "address1").send_keys("Спортивная, 18")
    driver.find_element("name", "postcode").send_keys("98989")
    driver.find_element("name", "city").send_keys("Лучший")
    driver.find_element("xpath", "//span[@class = 'select2-selection select2-selection--single']").click()
    driver.find_element("xpath", "//span[@class= 'select2-search select2-search--dropdown']/input[@type = 'search']").send_keys("united states")
    driver.find_element("xpath", "//ul[@class = 'select2-results__options']/li").click()
    driver.find_element("name", "email").send_keys(email)
    driver.find_element("name", "phone").send_keys("+7989987989")
    time.sleep(1)
    driver.find_element("name", "password").send_keys("тюльпанна")
    driver.find_element("name", "confirmed_password").send_keys("тюльпанна")
    driver.find_element("name", "create_account").click()
    driver.find_element("xpath", "//ul[@class = 'list-vertical'] // li[4]").click()

    driver.find_element("name", "email").send_keys(email)
    driver.find_element("name", "password").send_keys("тюльпанна")
    driver.find_element("name", "login").click()
    driver.find_element("xpath", "//ul[@class = 'list-vertical'] // li[4]").click()
    time.sleep(5)


def test_auth_user(driver): #авторизация пользователя
    driver.get("http://localhost/litecart/")
    driver.find_element("name", "email").send_keys("tulip@maill.ru")
    driver.find_element("name", "password").send_keys("тюльпанна")
    driver.find_element("name", "login").click()
    time.sleep(5)

def test_logout_user(driver): #выход из аккаунта пользователя
    driver.get("http://localhost/litecart/")
    driver.find_element("name", "email").send_keys("tulip@maill.ru")
    driver.find_element("name", "password").send_keys("тюльпанна")
    driver.find_element("name", "login").click()
    driver.find_element("xpath", "//ul[@class = 'list-vertical'] // li[4]").click()

