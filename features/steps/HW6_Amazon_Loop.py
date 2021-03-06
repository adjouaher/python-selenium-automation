from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException

BEST_SELLERS_LINKS = (By.CSS_SELECTOR, 'zg_tabs a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')

@given('Open amazon Best Sellers top icon page')
def open_bestsellers_top_icon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify Best Sellers 5 links are visible')
def verify_BestSellers_links_present(context):
    best_sellers_links = context.driver.find_elements(*BEST_SELLERS_LINKS)


    for x in range(len(best_sellers_links)):
        link = context.driver.find_elements(*BEST_SELLERS_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'