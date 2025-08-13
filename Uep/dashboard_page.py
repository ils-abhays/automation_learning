from selenium.webdriver.common.by import By
from base_page import BasePage

class DashboardPage(BasePage):
    USER_ICON = (By.XPATH, '//img[@alt="User Avatar" or contains(@class,"user")]')
    LOGOUT_BTN = (By.XPATH, '//span[text()="Logout" or contains(., "Sign out") or contains(., "Log out")]')

    def logout(self):
        self.click(self.USER_ICON)
        self.click(self.LOGOUT_BTN)
