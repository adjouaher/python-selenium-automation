from selenium.webdriver.common.by import By
from Pages.Base_page import Page


class MainPage(Page):
    # Amazon_Orders = (By.ID, '#nav-orders')
    # Cart_Icon = (By.ID, '#nav-cart-count')
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')

    def open_main_page(self):
        self.open_url('https://www.amazon.com/')

    def input_amazon_search(self):
        self.input_text('Key chain', *SEARCH_FIELD)

    def click_amazon_search_icon(self):
        self.click(*self.SEARCH_FIELD)

    def click_first_product(self):
        self.click(*self.PRODUCT_RESULT)
        e = self.wait.until(EC.element_to_be_clickable(PRODUCT_RESULT))
        e.click()

    def click_add_cart(self):
        self.clcik(*self.ADD_TO_CART_BTN)

