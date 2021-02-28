from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException

Best_Sellers_Top_Icon = (By.CSS_SELECTOR, "a[href*='zg_bs_tab']")
Best_Sellers_Icon = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab']")
New_Releases_Icon = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/gp/new-releases/ref=zg_bs_tab']")
New_MoversandShakers_Icon = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/gp/movers-and-shakers/ref=zg_bsms_tab']")
Most_Wished_Icon = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/gp/most-wished-for/ref=zg_bs_tab']")
Gift_Ideas_Icon = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/gp/most-gifted/ref=zg_bs_tab']")


@given('Open amazon Best Sellers top icon page')
def open_bestsellers_top_icon(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify Best Sellers menu icon is visible')
def verify_BestSellers_menu_present(context):
    e1 = context.driver.find_element(*Best_Sellers_Icon)
    context.driver.refresh()
    context.driver.find_element(*Best_Sellers_Icon).click()


@then('Verify New Releases menu icon is visible')
def verify_NewRelease_menu_present(context):
    e2 = context.driver.find_element(*New_Releases_Icon)
    context.driver.refresh()
    context.driver.find_element(*New_Releases_Icon).click()


@then('Verify Movers & Shakers menu icon is visible')
def verify_Movers_and_Shakers_menu_present(context):
    e3 = context.driver.find_element(*New_MoversandShakers_Icon)
    context.driver.refresh()
    context.driver.find_element(*New_MoversandShakers_Icon).click()


@then('Verify Most Wished For menu icon is visible')
def verify_Most_Wished_for_menu_present(context):
    e4 = context.driver.find_element(*Most_Wished_Icon)
    context.driver.refresh()
    context.driver.find_element(*Most_Wished.Icon).click()


@then('Verify Gift Ideas menu icon is visible')
def verify_Gift_Ideas_menu_present(context):
    e5 = context.driver.find_element(*Gift_Ideas_Icon)
    context.driver.refresh()
    context.driver.find_element(*Gift_Ideas_Icon).click()

