from selenium.webdriver.common.by import By
from Pages.Base_page import Page


class Signinpage(Page):
    Orders_click_result = (By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']/h1")

    def verify_Sign_in_page(self, Signinpage):
        self.verify_text(Signinpage, *self.Orders_click_result)


