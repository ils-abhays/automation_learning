
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import wait

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Prevent extra blank tab
options.add_argument("--disable-blink-features=AutomationControlled")  # Optional: cleaner launch

# Launch browser
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://dev-admin.uepviewer.com/")
time.sleep(2)
# Login
driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys("anuuu@gmail.com")
driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("Anee@123")
driver.find_element(By.XPATH, '//button[text()="LOGIN"]').click()
time.sleep(5)

driver.find_element(By.XPATH, '//label[text()="Staff"]').click()
driver.find_element(By.XPATH, '//button[text()="+ Add Staff"]').click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Full Name']").send_keys("Auto Customer")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']").send_keys("auto.customer@example.com")
driver.find_element(By.XPATH, "//input[@placeholder='Enter Number']").send_keys("(999) 888-7777")
time.sleep(1)
driver.find_element(By.XPATH, '//select[@name="user_role"]/option[text()="Manager"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[@aria-label="Close"]').click()
# driver.find_element(By.XPATH, '//button[span[text()="Add"]]').click()
time.sleep(3)

# Search field

# Month dropdown click
driver.find_element(By.XPATH, "//input[@placeholder='Created On']").click()
time.sleep(1)
# Date filter
# Month select
driver.find_element(By.XPATH, '//button[@class="ant-picker-month-btn"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="May"]').click()
time.sleep(2)
# Date select
driver.find_element(By.XPATH, '//div[@class="ant-picker-cell-inner" and text()="1"]').click()
time.sleep(2)

# # Search field
# driver.find_element(By.XPATH, "//input[@placeholder='Name, Email, Tel']").send_keys("Demo")
# time.sleep(2)
# Toggle Active/Inactive
driver.find_element(By.XPATH, '//input[@id="live"]/following-sibling::span[@class="checkmark"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//input[@id="live"]/following-sibling::span[@class="checkmark"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//input[@id="not_live"]/following-sibling::span[@class="checkmark"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//input[@id="not_live"]/following-sibling::span[@class="checkmark"]').click()
time.sleep(2)
# driver.find_element(By.XPATH, "//span[contains(text(),'Active')]").click()
# Search field
driver.find_element(By.XPATH, "//input[@placeholder='Name, Email, Tel']").send_keys("Mayank")
time.sleep(4)
# View
# driver.find_element(By.XPATH, '//img[@alt="read"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//button[contains(@class, "back-btn")]').click()
# time.sleep(2)
# Edit
driver.find_element(By.XPATH, '//img[@alt="edit"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[span[text()="Add"]]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//img[@alt="deleteicon"]').click()
time.sleep(2)
# Cancel Delete
driver.find_element(By.XPATH, '//button[span[text()="Cancel"]]').click()
# driver.find_element(By.XPATH, '//button[span[text()="Delete"]]').click()
time.sleep(2)
# Status toggle
driver.find_element(By.XPATH, '//button[@role="switch" and contains(@class, "ant-switch")]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[@role="switch" and contains(@class, "ant-switch")]').click()
