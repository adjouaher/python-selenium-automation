from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.implicitly_wait(4)

driver.get('https://www.amazon.com/gp/help/customer/display.html ')

search_field = driver.find_element(By.ID, 'helpsearch')
search_field.send_keys('cancel order'+'\n')

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'expected {expected_text}, but got {actual_text}'

driver.quit()

***

Amazon logo, search by Xpath, $x("//div[@class='a-section a-spacing-medium a-text-center']//i[contains(@class,'a-icon a-icon-logo')]")
Email field, search by ID, $x("//input[@id='ap_email']")
Continue button, search by id, $x("//input[@id='continue']")
Need help link, search by Xpath, $x("//span[@class='a-expander-prompt']")
Forgot your password link, search by ID, $x("//div[@aria-expanded='true']//a[contains(@id,'auth-fpp-link-bottom')]")
Other issues with Sign-In link, search by ID, $x("//div[@aria-expanded='true']//a[contains(@id,'ap-other-signin-issues-link')]")
Create your Amazon account button, search by ID, $x("//span[@class='a-button-inner']//a[contains(@id,'createAccountSubmit')]")
Conditions of use link, search by Xpath, $x("//div[@id='legalTextRow']//a[contains(@href, '/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088')]")
Privacy Notice link, search by xpath, $x("//div[@id='legalTextRow']//a[contains(@href,'/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496')]")

***






