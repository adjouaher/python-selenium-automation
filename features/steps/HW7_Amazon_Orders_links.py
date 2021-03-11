from selenium.webdriver.common.by import By
from behave import given, when, then


Amazon_Orders = (By.ID, '#nav-orders')
Sign_in_result = (By.XPATH, "//div[@class='a-box']//h1")


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.main_page.click_amazon_orders()


@then('Verify Sign In page is opened')
def verify_Sign_in_page(context, SignIn):
    context.app.Sign_in_page.verify_Sign_in_page(Orders_click_result)



Amazon_Orders = (By.ID, '#nav-orders')
Sign_in_result = (By.XPATH, "//div[@class='a-box']//h1")


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.main_page.click_amazon_orders()

@then('Verify Sign In page is opened')
def verify_Sign_in_page(context):
    context.app.Sign_in_page.verify_Sign_in_page(Orders_click_result)
