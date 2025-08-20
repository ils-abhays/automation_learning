from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProducerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- Locators ----------
    login_email = (By.XPATH, '//input[@placeholder="Email"]')
    login_password = (By.XPATH, '//input[@placeholder="Password"]')
    login_button = (By.XPATH, '//button[text()="LOGIN"]')

    producers_tab = (By.XPATH, '//label[text()="Producers"]')
    add_producer_button = (By.XPATH, '//button[text()="+ Add Producer"]')
    close_popup_button = (By.XPATH, '//button[@aria-label="Close"]')

    full_name = (By.XPATH, "//input[@placeholder='Enter Full Name']")
    event_producer = (By.XPATH, "//input[@placeholder='Enter Event Producer']")
    address = (By.XPATH, "//input[@placeholder='Enter Full Address']")
    email = (By.XPATH, "//input[@placeholder='Enter Email']")
    number = (By.XPATH, "//input[@placeholder='Enter Number']")

    created_on_field = (By.XPATH, "//input[@placeholder='Created On']")
    month_btn = (By.XPATH, '//button[@class="ant-picker-month-btn"]')
    may_month = (By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="May"]')
    date_1 = (By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="1"]')

    live_toggle = (By.XPATH, '//input[@id="live"]/following-sibling::span[@class="checkmark"]')
    not_live_toggle = (By.XPATH, '//input[@id="not_live"]/following-sibling::span[@class="checkmark"]')

    search_field = (By.XPATH, "//input[@placeholder='Name, Email, Tel']")

    view_icon = (By.XPATH, '//img[@alt="read"]')
    edit_icon = (By.XPATH, '//img[@alt="edit"]')
    delete_icon = (By.XPATH, '//img[@alt="deleteicon"]')

    cancel_delete_button = (By.XPATH, '//button[span[text()="Cancel"]]')
    add_button = (By.XPATH, '//button[span[text()="Add"]]')
    status_switch = (By.XPATH, '//button[@role="switch" and contains(@class, "ant-switch")]')

    # ---------- Actions ----------
    def login(self, email, password):
        self.wait.until(EC.presence_of_element_located(self.login_email)).send_keys(email)
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def open_producer_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.producers_tab)).click()

    def add_producer(self, name, producer, address, email, number):
        self.wait.until(EC.element_to_be_clickable(self.add_producer_button)).click()
        self.wait.until(EC.presence_of_element_located(self.full_name)).send_keys(name)
        self.driver.find_element(*self.event_producer).send_keys(producer)
        self.driver.find_element(*self.address).send_keys(address)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.number).send_keys(number)
        time.sleep(1)
        self.driver.find_element(*self.close_popup_button).click()

    def apply_date_filter(self):
        self.driver.find_element(*self.created_on_field).click()
        self.driver.find_element(*self.month_btn).click()
        self.wait.until(EC.element_to_be_clickable(self.may_month)).click()
        self.wait.until(EC.element_to_be_clickable(self.date_1)).click()

    def toggle_status(self):
        time.sleep(1)
        self.driver.find_element(*self.live_toggle).click()
        time.sleep(1)
        self.driver.find_element(*self.live_toggle).click()
        time.sleep(1)
        self.driver.find_element(*self.not_live_toggle).click()
        time.sleep(1)
        self.driver.find_element(*self.not_live_toggle).click()

    def search_producer(self, keyword):
        field = self.wait.until(EC.presence_of_element_located(self.search_field))
        field.clear()
        field.send_keys(keyword)
        time.sleep(2)

    def view_producer(self):
        self.wait.until(EC.element_to_be_clickable(self.view_icon)).click()
        time.sleep(1)
        self.driver.find_element(*self.close_popup_button).click()

    def edit_producer(self):
        self.wait.until(EC.element_to_be_clickable(self.edit_icon)).click()
        time.sleep(1)
        self.driver.find_element(*self.add_button).click()

    def delete_producer(self):
        self.wait.until(EC.element_to_be_clickable(self.delete_icon)).click()
        time.sleep(1)
        self.driver.find_element(*self.cancel_delete_button).click()

    def toggle_producer_status(self, times=1):
        print("⚡ Toggling Status Switch...")
        switch_xpath = '//button[@role="switch" and contains(@class, "ant-switch")]'
        for i in range(times):
            print(f"   ⏳ Waiting before toggle {i+1}...")
            time.sleep(2)  # wait before toggle
            elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, switch_xpath)))
            elem.click()
            print(f"   🔀 Toggled {i+1}/{times}")
            time.sleep(3)  # wait after toggle

# ------------------ MAIN SCRIPT ------------------
if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://dev-admin.uepviewer.com/")

    page = ProducerPage(driver)

    # Login
    page.login("anuuu@gmail.com", "Anee@123")
    time.sleep(3)

    # Navigate to Producers
    page.open_producer_tab()
    time.sleep(2)

    # Add Producer
    page.add_producer("Auto Customer", "auto.customer@example.com", "Test Address", "auto.customer@example.com", "(999) 888-7777")

    # Apply Date Filter
    page.apply_date_filter()

    # Toggle Active/Inactive
    page.toggle_status()

    # Search Producer
    page.search_producer("UTV")

    # View Producer
    page.view_producer()

    # Edit Producer
    page.edit_producer()

    # Delete Producer (Cancel only)
    page.delete_producer()

    # Search Producer
    page.search_producer("UTV")

    # Status Toggle
    page.toggle_producer_status(times=2)

    print("✅ Producer module automation completed successfully. Browser remains open.")
