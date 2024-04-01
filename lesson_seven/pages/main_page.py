from pages.base_page import BasePage


card_selector = ("xpath", "//div[@class= 'image-wrapper']")
card_selectors = ("xpath", "//li[@class= 'product column shadow hover-light']")




class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get("http://localhost/litecart/en/")

    def card_products(self):
        return self.finds(card_selectors)

    def card_product(self):
        return self.find(card_selector)

    def click_card_product(self):
        self.card_product().click()

