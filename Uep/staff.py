import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StaffPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ---------- Locators ----------
    login_email = (By.XPATH, '//input[@placeholder="Email"]')
    login_password = (By.XPATH, '//input[@placeholder="Password"]')
    login_button = (By.XPATH, '//button[text()="LOGIN"]')

    staff_tab = (By.XPATH, '//label[text()="Staff"]')
    add_staff_button = (By.XPATH, '//button[text()="+ Add Staff"]')
    close_popup_button = (By.XPATH, '//button[@aria-label="Close"]')

    full_name = (By.XPATH, "//input[@placeholder='Enter Full Name']")
    email = (By.XPATH, "//input[@placeholder='Enter Email']")
    number = (By.XPATH, "//input[@placeholder='Enter Number']")
    role_dropdown = (By.XPATH, '//select[@name="user_role"]/option[text()="Manager"]')

    created_on_field = (By.XPATH, "//input[@placeholder='Created On']")
    month_btn = (By.XPATH, '//button[@class="ant-picker-month-btn"]')
    may_month = (By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="May"]')
    date_1 = (By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="1"]')

    live_toggle = (By.XPATH, '//input[@id="live"]/following-sibling::span[@class="checkmark"]')
    not_live_toggle = (By.XPATH, '//input[@id="not_live"]/following-sibling::span[@class="checkmark"]')

    search_field = (By.XPATH, "//input[@placeholder='Name, Email, Tel']")
    table_rows = (By.XPATH, '//tr[contains(@class,"ant-table-row")]')

    add_button = (By.XPATH, '//button[span[text()="Add"]]')
    status_switch = (By.XPATH, '//button[@role="switch" and contains(@class, "ant-switch")]')
    cancel_delete_button = (By.XPATH, '//button[span[text()="Cancel"]]')

    # ---------- Actions ----------
    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(self.login_email)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.login_password)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()
        time.sleep(3)  # wait for dashboard to load

    def open_staff_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.staff_tab)).click()
        time.sleep(2)  # wait for staff tab to load

    def add_staff(self, name, email, number):
        self.wait.until(EC.element_to_be_clickable(self.add_staff_button)).click()
        time.sleep(1)
        self.wait.until(EC.visibility_of_element_located(self.full_name)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.email)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.number)).send_keys(number)
        self.wait.until(EC.element_to_be_clickable(self.role_dropdown)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
        time.sleep(2)

    def apply_date_filter(self):
        self.wait.until(EC.element_to_be_clickable(self.created_on_field)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.month_btn)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.may_month)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.date_1)).click()
        time.sleep(2)  # wait for table to reload

    def toggle_status(self):
        self.wait.until(EC.element_to_be_clickable(self.live_toggle)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.live_toggle)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.not_live_toggle)).click()
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(self.not_live_toggle)).click()
        time.sleep(1)

    def search_staff(self, keyword):
        field = self.wait.until(EC.presence_of_element_located(self.search_field))
        field.clear()
        field.send_keys(keyword)
        time.sleep(2)  # wait for search results to appear

    # ---------- Row-specific actions ----------
    def view_staff(self, keyword):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.table_rows))
        target_row = None
        for row in rows:
            if keyword.lower() in row.text.lower():
                target_row = row
                break
        if target_row:
            view_icon = target_row.find_element(By.XPATH, './/img[@alt="read"]')
            self.wait.until(EC.element_to_be_clickable(view_icon)).click()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable(self.close_popup_button)).click()
            time.sleep(1)
        else:
            print(f"⚠️ No staff found to view with keyword: {keyword}")

    def edit_staff(self, keyword):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.table_rows))
        target_row = None
        for row in rows:
            if keyword.lower() in row.text.lower():
                target_row = row
                break
        if target_row:
            edit_icon = target_row.find_element(By.XPATH, './/img[@alt="edit"]')
            self.wait.until(EC.element_to_be_clickable(edit_icon)).click()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
            time.sleep(1)
        else:
            print(f"⚠️ No staff found to edit with keyword: {keyword}")

    def delete_staff(self, keyword):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.table_rows))
        target_row = None
        for row in rows:
            if keyword.lower() in row.text.lower():
                target_row = row
                break
        if target_row:
            delete_icon = target_row.find_element(By.XPATH, './/img[@alt="deleteicon"]')
            self.wait.until(EC.element_to_be_clickable(delete_icon)).click()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable(self.cancel_delete_button)).click()
            time.sleep(1)
        else:
            print(f"⚠️ No staff found to delete with keyword: {keyword}")

    def toggle_staff_status(self, times=1):
        print("⚡ Toggling Staff Status Switch...")
        for i in range(times):
            time.sleep(3)
            elem = self.wait.until(EC.element_to_be_clickable(self.status_switch))
            elem.click()
            print(f"   🔀 Toggled {i+1}/{times}")
            time.sleep(2)

# ------------------ MAIN SCRIPT ------------------
if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://dev-admin.uepviewer.com/")

    page = StaffPage(driver)

    # Login
    page.login("anuuu@gmail.com", "Anee@123")

    # Navigate to Staff
    page.open_staff_tab()

    # Add Staff
    page.add_staff("Auto Staff", "auto.staff@example.com", "(999) 888-6666")

    # Apply Date Filter
    page.apply_date_filter()

    # Toggle Active/Inactive
    page.toggle_status()

    # Search Staff
    page.search_staff("Mayank")

    # View Staff
    # page.view_staff("Mayank")

    # Edit Staff
    page.edit_staff("Mayank")

    # Delete Staff (Cancel only)
    page.delete_staff("Mayank")

    # Search Staff Again
    page.search_staff("Mayank")

    # Status Toggle
    page.toggle_staff_status(times=2)

    print("✅ Staff module automation completed successfully. Browser remains open.")
