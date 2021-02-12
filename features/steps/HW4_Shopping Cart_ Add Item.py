from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

PRODUCT_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
CART = (By.ID, 'nav-cart-count')


@when('Imput Mouse into Amazon search field')
def input_amazon_search(context):
    search_field = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    search_field.send_keys('Mouse')


@when('click on Amazon search icon')
def click_search_amazon(context):
    search_icon = context.driver.find_element(By.ID, 'nav-search-submit-button')
    search_icon.click()


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_RESULT).click()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@then('Verify cart has {expected_count} Item')
def verify_cart_count(context, expected_count):
    cart_count = context.driver.find_element(*CART).text
    assert expected_count == cart_count, f'Expected {expected_count} items but got {cart_count}'
