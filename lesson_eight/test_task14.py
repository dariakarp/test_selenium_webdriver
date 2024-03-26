import time
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(10)
    request.addfinalizer(wd.quit)
    return wd
def test_click_on_all_links(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://localhost/litecart/admin") #вход в админку
    driver.find_element("name", "username").send_keys("admin")
    driver.find_element("name", "password").send_keys("admin")
    driver.find_element("name", "login").click()

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries") #вход на страницу со странами
    driver.find_element("xpath", "//a[@class = 'button']").click()#клик на кнопку "добавить новую страну"

    old_windows = driver.window_handles #получаю список окон (пока только одно окно)
    all_links = driver.find_elements("xpath", "//td[@id = 'content']//td//a[not(@id = 'address-format-hint')]")#нахожу все ссылки, на которые нужно кликнуть
    for i in range(len(all_links)):

        all_links = driver.find_elements("xpath","//td[@id = 'content']//td//a[not(@id = 'address-format-hint')]")  # нахожу все ссылки, на которые нужно кликнуть
        links = all_links[i]
        links.click()#кликаю на иконку для открытия нового окна
        wait.until(EC.number_of_windows_to_be(2))# жду пока количество окон не станет равным 2
        all_windows = driver.window_handles #получаю список всех окон
        new_windows = [x for x in all_windows if x not in old_windows]#получаю второе окно
        driver.switch_to.window(new_windows[0])#переключаюсь в новое окно
        driver.close()
        driver.switch_to.window(old_windows[0])#переключаюсь в первое (изначальное) окно









