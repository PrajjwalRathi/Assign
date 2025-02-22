from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = (By.ID, "email")
        self.password = (By.ID, "pass")
        self.login_button = (By.ID, "send2")

    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
