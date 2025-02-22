from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # ✅ Explicit wait for all elements
        self.first_name = (By.ID, "firstname")
        self.last_name = (By.ID, "lastname")
        self.email = (By.ID, "email_address")
        self.password = (By.ID, "password")
        self.confirm_password = (By.ID, "password-confirmation")
        self.signup_button = (By.CSS_SELECTOR, "button.action.submit.primary")

    def enter_first_name(self, fname):
        self.wait.until(EC.presence_of_element_located(self.first_name)).send_keys(fname)

    def enter_last_name(self, lname):
        self.wait.until(EC.presence_of_element_located(self.last_name)).send_keys(lname)

    def enter_email(self, email):
        self.wait.until(EC.presence_of_element_located(self.email)).send_keys(email)

    def enter_password(self, pwd):
        self.wait.until(EC.presence_of_element_located(self.password)).send_keys(pwd)

    def enter_confirm_password(self, confirm_pwd):
        self.wait.until(EC.presence_of_element_located(self.confirm_password)).send_keys(confirm_pwd)

    def click_signup(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_button)).click()
