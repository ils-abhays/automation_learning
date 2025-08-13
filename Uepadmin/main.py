from pywin.mfc.dialog import PrintDialog
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import Select
import time

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

# Grab and print values one by one
cards = driver.find_elements(By.CLASS_NAME, "dashboard_report_card")
total_customers = cards[0].find_element(By.CLASS_NAME, "count_name").text
total_customerscounts = cards[0].find_element(By.CLASS_NAME, "counts").text
total_orders = cards[1].find_element(By.CLASS_NAME, "count_name").text
total_orderscounts = cards[1].find_element(By.CLASS_NAME, "counts").text
completed_order = cards[2].find_element(By.CLASS_NAME, "count_name").text
completed_ordercounts = cards[2].find_element(By.CLASS_NAME, "counts").text
pending_orders = cards[3].find_element(By.CLASS_NAME, "count_name").text
pending_orderscounts = cards[3].find_element(By.CLASS_NAME, "counts").text
events_created = cards[4].find_element(By.CLASS_NAME, "count_name").text
events_createdcounts = cards[4].find_element(By.CLASS_NAME, "counts").text
# total_orders = driver.find_element(By.XPATH, '//div[contains(text(),"Total Orders")]/preceding-sibling::div').text
# completed_orders = driver.find_element(By.XPATH, '//div[contains(text(),"Completed Orders")]/preceding-sibling::div').text
# pending_orders = driver.find_element(By.XPATH, '//div[contains(text(),"Pending Orders")]/preceding-sibling::div').text
# events_created = driver.find_element(By.XPATH, '//div[contains(text(),"Events Created")]/preceding-sibling::div').text

# Print results
print("Overall Reports")
print(total_customers + ": " + total_customerscounts)
print(total_orders + ": " + total_orderscounts)
print(completed_order + ": " + completed_ordercounts)
print(pending_orders + ": " + pending_orderscounts)
print(events_created + ": " + events_createdcounts)
time.sleep(2)

driver.find_element(By.XPATH, '//label[text()="Events"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//button[text()="+ Create Event"]').click()
time.sleep(1)
# event_code = input("Enter Event Code: ")
driver.find_element(By.XPATH, '//input[@name="event_code"]').click()
driver.find_element(By.XPATH, '//input[@name="event_code"]').send_keys("UE2025")

driver.find_element(By.XPATH, '//input[@name="event_title"]').click()
driver.find_element(By.XPATH, '//input[@name="event_title"]').send_keys("UE Automation")
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Start Date']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Start Date']").send_keys("07/28/2025" + Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='End Date']").click()
driver.find_element(By.XPATH, "//input[@placeholder='End Date']").send_keys("07/29/2025" + Keys.ENTER)
time.sleep(1)
driver.find_element(By.NAME, "event_producer").click()
time.sleep(2)
driver.find_element(By.XPATH, "//option[text()='UTV']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Event Comments']").click()
driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Event Comments']").send_keys("Testing")
time.sleep(1)

driver.find_element(By.XPATH, '//label[text()="Cheer"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[text()="+ Add Teams"]').click()
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@placeholder='Enter team no.'])[1]").click()
driver.find_element(By.XPATH, "(//input[@placeholder='Enter team no.'])[1]").send_keys("8188")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@placeholder='Enter team name'])[1]").click()
driver.find_element(By.XPATH, "(//input[@placeholder='Enter team name'])[1]").send_keys("Test8188" + Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@placeholder='Enter team no.'])[2]").click()
driver.find_element(By.XPATH, "(//input[@placeholder='Enter team no.'])[2]").send_keys("9199")
time.sleep(1)
driver.find_element(By.XPATH, "(//input[@placeholder='Enter team name'])[2]").click()
driver.find_element(By.XPATH, "(//input[@placeholder='Enter team name'])[2]").send_keys("Test9199")
time.sleep(2)
driver.find_element(By.XPATH, '//button[span[text()="Add"]]').click()
time.sleep(1)
driver.find_element(By.XPATH, '(//label[text()="Yes"])[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '(//label[text()="Yes"])[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, '(//label[text()="Yes"])[3]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//label[text()="Active"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//button[text()="Save"]').click()
time.sleep(4)


# Go to Files
driver.find_element(By.XPATH, '//label[text()="Files"]').click()

# Search
search_input = driver.find_element(By.NAME, "eventSearchParam")
search_input.send_keys("MD2024")
search_input.send_keys(Keys.ENTER)
time.sleep(4)
driver.find_element(By.XPATH, '//img[@alt="read"]').click()

time.sleep(4)
driver.find_element(By.XPATH, '//div[@class="card-header d-flex align-items-center"]//div[contains(@class, "card-heading") and contains(text(), "0001")]').click()

print("✅ Script completed. Browser is closed.")
driver.quit()

