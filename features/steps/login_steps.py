from behave import given, when, then
from pages.login_page import LoginPage

@given('the user is on the login page')
def step_user_on_login_page(context):
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    context.login_page = LoginPage(context.driver)

@when('the user enters valid login credentials')
def step_user_enters_login_details(context):
    context.login_page.enter_email("testuser@example.com")
    context.login_page.enter_password("Test@1234")

@when('clicks the login button')
def step_user_clicks_login(context):
    context.login_page.click_login()

@then('the user should be logged in successfully')
def step_user_logged_in(context):
    assert "My Account" in context.driver.page_source
