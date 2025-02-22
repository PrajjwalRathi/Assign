from behave import given, when, then
from pages.signup_page import SignupPage

@given('the user is on the signup page')
def step_user_on_signup_page(context):
    context.driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    context.signup_page = SignupPage(context.driver)

@when('the user enters valid signup details')
def step_user_enters_signup_details(context):
    context.signup_page.enter_first_name("test")
    context.signup_page.enter_last_name("tttser")
    context.signup_page.enter_email("eter@example.com")
    context.signup_page.enter_password("Test@1234")
    context.signup_page.enter_confirm_password("Test@1234")

@when('clicks the signup button')
def step_user_clicks_signup(context):
    context.signup_page.click_signup()

@then('the user account should be created successfully')
def step_user_account_created(context):
    assert "Thank you for registering" in context.driver.page_source
