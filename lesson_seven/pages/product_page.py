from pages.base_page import BasePage



select_size_in_product = ("xpath", "//select[@name= 'options[Size]']")
select_size_option_in_product = ("xpath", "//select[@name= 'options[Size]']/option[3]")
button_add_card = ("xpath", "//button[@name = 'add_cart_product']")
checkout = ("xpath", "//div[@id ='cart']/a[3]")

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_size(self):
        return self.find(select_size_in_product)

    def click_select_size(self):
        self.select_size().click()

    def select_size_option(self):
        return self.find(select_size_option_in_product)

    def click_select_size_option(self):
        self.select_size_option().click()

    def button(self):
        return self.find(button_add_card)

    def click_button(self):
        self.button().click()

    def button_checkout(self):
        return self.find(checkout)

    def click_button_checkout(self):
        self.button_checkout().click()



