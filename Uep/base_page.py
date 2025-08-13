from utils import wait_and_click, wait_and_type, wait_for_visibility

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        wait_and_click(self.driver, locator)

    def type(self, locator, text):
        wait_and_type(self.driver, locator, text)

    def is_visible(self, locator):
        return wait_for_visibility(self.driver, locator)
