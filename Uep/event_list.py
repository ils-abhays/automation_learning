import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventListingPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click(self, xpath):
        """Reusable click with wait"""
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elem.click()
        return elem

    def type(self, xpath, text):
        """Reusable input with wait"""
        elem = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        elem.clear()
        elem.send_keys(text)
        return elem

    # --------------------
    # LOGIN + NAVIGATION
    # --------------------
    def login(self, email, password):
        print("🔐 Logging in...")
        self.type('//input[@placeholder="Email"]', email)
        self.type('//input[@placeholder="Password"]', password)
        self.click('//button[text()="LOGIN"]')

    def go_to_events(self):
        print("📂 Navigating to Events Page...")
        self.click('//label[text()="Events"]')

    # --------------------
    # EVENT ACTIONS
    # --------------------
    def filter_by_date(self, month: str, day: str):
        print(f"📅 Applying Date Filter: {month} {day}")
        self.click("//input[@placeholder='Created On']")
        self.click('//button[@class="ant-picker-month-btn"]')
        self.click(f'//div[@class="ant-picker-cell-inner" and text()="{month}"]')
        self.click(f'//div[@class="ant-picker-cell-inner" and text()="{day}"]')

    def toggle_active_inactive(self):
        print("🔄 Toggling Active/Inactive...")
        time.sleep(2)
        self.click('//input[@id="live"]/following-sibling::span[@class="checkmark"]')
        time.sleep(2)
        self.click('//input[@id="live"]/following-sibling::span[@class="checkmark"]')
        time.sleep(2)
        self.click('//input[@id="not_live"]/following-sibling::span[@class="checkmark"]')
        time.sleep(2)
        self.click('//input[@id="not_live"]/following-sibling::span[@class="checkmark"]')
        time.sleep(2)

    def search_event(self, code: str):
        print(f"🔍 Searching Event: {code}")
        self.type("//input[@placeholder='Event Code, Title']", code)
        time.sleep(2)  # small pause for results

    def select_producer(self, producer: str):
        print(f"🎬 Selecting Producer: {producer}")
        self.click(f'//select[@name="producerName"]/option[text()="{producer}"]')

    def view_event(self):
        print("👁️ Viewing Event...")
        self.click('//img[@alt="read"]')
        self.click('//button[@aria-label="Close"]')

    def edit_event(self):
        print("✏️ Editing Event...")
        self.click('//img[@alt="edit"]')
        self.click('//button[text()="Update"]')

    def delete_event(self, confirm=False):
        print("🗑️ Deleting Event...")
        self.click('//img[@alt="deleteicon"]')
        if confirm:
            self.click('//button[span[text()="Delete"]]')
        else:
            self.click('//button[span[text()="Cancel"]]')

        # ✅ After delete/cancel → also click Update
        print("♻️ Updating after Delete/Cancel...")
        time.sleep(2)
        self.click('//button[text()="Update"]')
        time.sleep(2)

    def toggle_internet(self, times=1):
        print("⚡ Toggling Status Switch...")
        switch_xpath = '(//button[@role="switch" and contains(@class, "ant-switch")])[1]'
        for i in range(times):
            print(f"   ⏳ Waiting before toggle {i+1}...")
            time.sleep(2)  # wait before toggle
            elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, switch_xpath)))
            elem.click()
            print(f"   🔀 Toggled {i+1}/{times}")
            time.sleep(3)  # wait after toggle

    def toggle_kiosk(self, times=1):
        print("⚡ Toggling Status Switch...")
        switch_xpath = '(//button[@role="switch" and contains(@class, "ant-switch")])[2]'
        for i in range(times):
            print(f"   ⏳ Waiting before toggle {i+1}...")
            time.sleep(2)  # wait before toggle
            elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, switch_xpath)))
            elem.click()
            print(f"   🔀 Toggled {i+1}/{times}")
            time.sleep(3)  # wait after toggle

    def toggle_active(self, times=1):
        print("⚡ Toggling Status Switch...")
        switch_xpath = '(//button[@role="switch" and contains(@class, "ant-switch")])[3]'
        for i in range(times):
            print(f"   ⏳ Waiting before toggle {i+1}...")
            time.sleep(2)  # wait before toggle
            elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, switch_xpath)))
            elem.click()
            print(f"   🔀 Toggled {i+1}/{times}")
            time.sleep(3)  # wait after toggle

# =============== USAGE ==================
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://dev-admin.uepviewer.com/")   # Login page
    driver.maximize_window()

    events = EventListingPage(driver)

    # LOGIN
    events.login("anuuu@gmail.com", "Anee@123")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//label[text()="Events"]'))
    )

    # NAVIGATE TO EVENTS
    events.go_to_events()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Event Code, Title']"))
    )

    # EVENT ACTIONS
    events.filter_by_date("May", "1")
    events.toggle_active_inactive()
    events.search_event("NC2024")
    events.select_producer("All Star")
    events.view_event()
    events.edit_event()
    events.delete_event(confirm=False)  # ❌ Cancel delete but then Update
    events.search_event("NC2024")
    events.toggle_internet(times=2)
    events.toggle_kiosk(times=2)
    events.toggle_active(times=2)
    print("✅ Event Listing automation completed.")
    time.sleep(3)
    driver.quit()
