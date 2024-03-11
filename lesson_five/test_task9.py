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

def test_sorted_zones(driver):
    driver.get("http://localhost/litecart/admin")
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()


    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    countries = driver.find_elements("xpath", "//tr[@class = 'row']/td[3]/a") #все элементы с названиями стран

    for i in range(len(countries)):
        countries = driver.find_elements("xpath", "//tr[@class = 'row']/td[3]/a")
        country = countries[i]
        country.click()
        zones = driver.find_elements("xpath", "//*[contains(@name, '[zone_code]')]//option[@selected = 'selected']") #нахожу выбранный в выпадающем списке веб-элемент с атрибутом selected = 'selected'
        list_zone = []

        for j in range(len(zones)):
            zone = zones[j].get_attribute("text") #для каждой зоны получаю наименование выбранной страны в выпадающем списке
            list_zone.append(zone) #в список кладу наименования страны

        sorted_list_zone = sorted(list_zone) #сортирую в алфавитном порядке
        assert sorted_list_zone == list_zone

        driver.back()

