from selenium.webdriver.common.by import By
from base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Enter your email" or @placeholder="Email"]')
    SUBMIT_BTN = (By.XPATH, '//button[contains(., "Send") or contains(., "Reset") or contains(., "Submit")]')

    def reset_password(self, email):
        self.type(self.EMAIL_INPUT, email)
        self.click(self.SUBMIT_BTN)
