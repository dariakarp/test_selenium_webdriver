import time

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd

def test_name_in_main_page_and_name_in_product(driver):
    driver.get("http://localhost/litecart/en/")
    name_in_main_page = driver.find_element("xpath", "//div[@id = 'box-campaigns']//div[@class = 'name']").text #название товара на карточке товара

    driver.find_element("xpath", "//div[@id = 'box-campaigns']//div[@class = 'name']").click()
    name_in_product = driver.find_element("xpath", "// div[ @ id = 'box-product'] // h1").text #название товара в карточке товара

    assert name_in_main_page == name_in_product



def test_price_in_main_page_and_name_in_product(driver):
    driver.get("http://localhost/litecart/en/")
    regular_price = driver.find_element("xpath", "//div[@id = 'box-campaigns']//s[@class='regular-price']").get_attribute("textContent")
    campaign_price = driver.find_element("xpath", "//div[@id = 'box-campaigns']//strong[@class='campaign-price']").get_attribute("textContent")
    driver.find_element("xpath", "//div[@id = 'box-campaigns']//div[@class = 'name']").click()

    regular_price_in_product = driver.find_element("xpath", "//div[@id = 'box-product']//s").get_attribute("textContent")
    campaign_price_in_product = driver.find_element("xpath", "//div[@id = 'box-product']//strong[@class='campaign-price']").get_attribute("textContent")

    assert regular_price == regular_price_in_product
    assert campaign_price == campaign_price_in_product

def test_price(driver): #проверка, что у первого товара в блоке Campaigns обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
    driver.get("http://localhost/litecart/en/")
    regular_price = driver.find_element("xpath","//div[@id = 'box-campaigns']//s[@class='regular-price']").value_of_css_property("color") #Получаю цвет значения цены в формате RGBA
    text_decoration = driver.find_element("xpath", "//div[@id = 'box-campaigns']//s[@class='regular-price']").value_of_css_property("text-decoration")#Получаю значение line-through solid rgb(119, 119, 119), которое соответствует перечеркнутому значению

    color = Color.from_string(regular_price)
    assert color.red == color.green == color.blue# серый цвет это когда rgb совпадают


def test_color_in_Campaigns(driver): #проверка, что цена жирная и красная на странице в блоке Campaigns
    driver.get("http://localhost/litecart/en/")
    campaign_price = driver.find_element("xpath", "//div[@id = 'box-campaigns']//strong[@class='campaign-price']").value_of_css_property('color')
    campaign_price_font_weight = driver.find_element("xpath", "//div[@id = 'box-campaigns']//strong[@class='campaign-price']").value_of_css_property('font-weight')
    color = Color.from_string(campaign_price)
    assert color.green == color.blue # красный цвет, если g и b равны 0
    assert int(campaign_price_font_weight) > 699 #жирными считаются значения больше или равны 700


def test_color_in_product(driver): #проверка, что цена жирная и красная на странице товара
    driver.get("http://localhost/litecart/en/")
    driver.find_element("xpath", "//div[@id = 'box-campaigns']//div[@class = 'name']").click()
    campaign_price = driver.find_element("xpath","//div[@id= 'box-product']//strong[@class = 'campaign-price']").value_of_css_property('color')
    campaign_price_font_weight = driver.find_element("xpath","//div[@id= 'box-product']//strong[@class = 'campaign-price']").value_of_css_property('font-weight')
    color = Color.from_string(campaign_price)
    assert color.green == color.blue  # красный цвет, если g и b равны 0
    assert int(campaign_price_font_weight) > 699  # жирными считаются значения больше или равны 700


def test_campaign_price_more_than_regular_price(driver): #проверка, что у товара в блоке Campaigns акционная цена больше, чем обычная
    driver.get("http://localhost/litecart/en/")
    campaign_price = driver.find_element("xpath","//div[@id = 'box-campaigns']//strong[@class = 'campaign-price']").value_of_css_property("font-size") #размер шрифта акционной цены
    regular_price = driver.find_element("xpath","//div[@id = 'box-campaigns']//s[@class='regular-price']").value_of_css_property("font-size")
    size_campaign_price = campaign_price.replace("px", "")
    size_regular_price = regular_price.replace("px", "")

    assert size_campaign_price > size_regular_price

def test_campaign_price_more_than_regular_price_in_product(driver): #проверка, что в карточке акционная цена больше, чем обычная
    driver.get("http://localhost/litecart/en/")
    driver.find_element("xpath", "//div[@id = 'box-campaigns']//div[@class = 'name']").click()
    campaign_price = driver.find_element("xpath","//div[@id= 'box-product']//strong[@class = 'campaign-price']").value_of_css_property("font-size") #размер шрифта акционной цены
    regular_price = driver.find_element("xpath","//div[@id= 'box-product']//s[@class = 'regular-price']").value_of_css_property("font-size")

    size_campaign_price = campaign_price.replace("px", "")
    size_regular_price = regular_price.replace("px", "")

    assert size_campaign_price > size_regular_price


