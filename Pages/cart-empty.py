from selenium.webdriver.common.by import By
from Pages.Base_page import Page


class CartEmptyPage(Page):
    Cart_Empty = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def verify_Sign_in_page(self, youramazoncartempty):
        self.verify_text(youramazoncartempty, *self.Cart_Empty)