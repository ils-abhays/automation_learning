from selenium.webdriver.common.by import By
from base_page import BasePage
from config import BASE_URL

class LoginPage(BasePage):
    EMAIL = (By.XPATH, '//input[@placeholder="Email"]')
    PASSWORD = (By.XPATH, '//input[@placeholder="Password"]')
    LOGIN_BTN = (By.XPATH, '//button[text()="LOGIN"]')
    FORGOT_PWD_LINK = (By.XPATH, '//a[contains(text(),"Forgot") or contains(text(),"forgot")]')

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, email, password):
        self.type(self.EMAIL, email)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def go_to_forgot_password(self):
        self.click(self.FORGOT_PWD_LINK)
