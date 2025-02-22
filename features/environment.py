from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    """Setup WebDriver before all tests"""
    print("Initializing WebDriver...")
    context.driver = webdriver.Chrome()

def after_all(context):
    """Close WebDriver after all tests"""
    if hasattr(context, "driver"):
        print("Closing WebDriver...")
        context.driver.quit()
