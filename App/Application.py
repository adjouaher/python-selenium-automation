from Pages.Main_Page import MainPage
from Pages.Sign_in_page import Signinpage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.cart_show_item = cartshowitem(self.driver)