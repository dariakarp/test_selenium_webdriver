from pages.base_page import BasePage

buttons_delete = ("xpath", "//form[@name='cart_form']//button[@name = 'remove_cart_item']")
table = ("xpath", "//div[@id = 'box-checkout-summary']")

class BasketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def delete(self):
        return self.find(buttons_delete)

    def click_delete(self):
        self.delete().click()

    def table(self):
        return self.find(table)