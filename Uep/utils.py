from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_click(driver, locator, timeout=15):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator)).click()

def wait_and_type(driver, locator, text, timeout=15):
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    element.clear()
    element.send_keys(text)

def wait_for_visibility(driver, locator, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
