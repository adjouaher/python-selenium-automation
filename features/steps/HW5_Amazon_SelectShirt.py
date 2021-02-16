from selenium.webdriver.common.by import By
from behave import given, when, then

SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
COLOR_OPTION = (By.CSS_SELECTOR, '#variation_color_name li')


@given('Open Amazon Shirt B08HQ6NK17 page')
def verify_amazon_shirt_page(context):
    context.driver.get(f'https://www.amazon.com/dp/B08HQ6NK17/')


@then('Verify user can click through colors')
def verify_can_select_colors(context):
    expected_colors = ['Blackgreyblue', 'Blackgreywhite', 'Blackgreyyellow', 'Blackgreynavy']
    colors = context.driver.find_elements(*COLOR_OPTION)

    for i in range(len(colors)):
        colors[i].click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        assert expected_colors[i] == selected_color, f'Expected (expected_colors[i]) but got (selected_color)'

