from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

wait = WebDriverWait(driver, 10)


def test_work_in_basket(driver):
    main_page = MainPage(driver)
    product_page = ProductPage(driver)
    basket_page = BasketPage(driver)
    main_page.open()

    product_in_box = 0
    for i in range(3):
        main_page.card_products() #нахожу карточки на главной странице
        main_page.click_card_product() #кликаю на первую карточку товара
        try:
            product_page.select_size() #нахожу селект
            product_page.click_select_size() #кликаю на селект
            product_page.click_select_size_option() #кликаю на значение в выпадающем списке
            product_page.click_button() #кликаю на добавить в корзину
        except NoSuchElementException:
            print("нет ошибки")
            product_page.click_button() #кликаю на добавить в корзину

        product_in_box += 1
        count_wait = str(product_in_box)
        wait.until(EC.text_to_be_present_in_element(("xpath", "//div[@id = 'cart']//span[@class = 'quantity']"), count_wait))
        driver.back()
    product_page.click_button_checkout() #клик на "Checkout" на корзину

    basket_page.delete()  # нахожу кнопки Удалить
    for j in range(len(basket_page.delete())):
        basket_page.table()  # нахожу таблицу по локатору
        basket_page.click_delete() #кликаю на кнопку delete
        wait.until(EC.staleness_of(table))  # жду пока талица обновится















