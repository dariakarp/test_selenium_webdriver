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
def test_sorted_countries(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()


    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    countries = driver.find_elements("xpath", "//tr[@class = 'row']//a[not(@title)]") #все элементы с названиями стран

    list_countries = [] #пустой список, чтобы положить туда значения атрибутов text по каждой стране

    for i in range(len(countries)):
        country = countries[i].get_attribute("text")
        list_countries.append(country)

    sorted_countries = sorted(list_countries)
    assert list_countries == sorted_countries

def test_zones_countries(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()


    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    zones = driver.find_elements("xpath", "//tr[@class = 'row']//td[6]")


    for i in range(len(zones)):
        countries = driver.find_elements("xpath","//tr[@class = 'row']//a[not(@title)]")  # все элементы с названиями стран
        zones = driver.find_elements("xpath", "//tr[@class = 'row']//td[6]") #все элементы с номерами зон
        zone = int(zones[i].get_attribute("textContent"))



        if zone != 0: #если зона не равна нулю, кликаю по названию страны этой зоны
            country = countries[i]
            country.click()
            list_countries = [] #пустой список, чтобы складывать туда значения стран

            country_in_countries = driver.find_elements("xpath", "//table[@id = 'table-zones']//td[3]/input[@type!='text']")
            for j in range(len(country_in_countries)):
                country_name = country_in_countries[j].get_attribute("value")
                list_countries.append(country_name)

            sorted_country_in_countries = sorted(list_countries)
            assert list_countries == sorted_country_in_countries
            driver.back()











