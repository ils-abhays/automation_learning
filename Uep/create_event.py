from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import openpyxl
import time

# ------------------------
# CONFIGURATION
# ------------------------
BASE_URL = "https://dev-admin.uepviewer.com/"
EXCEL_FILE = r"E:\PycharmProjects\PythonProject2\create_event_data.xlsx"
EMAIL = "anuuu@gmail.com"
PASSWORD = "Anee@123"

# ------------------------
# READ EVENT DATA
# ------------------------
workbook = openpyxl.load_workbook(EXCEL_FILE)
sheet = workbook.active
event_data = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    event_code, title, start_date, end_date, producer, comments, mode, team1_no, team1_name, team2_no, team2_name = row
    event_data.append({
        "event_code": str(event_code or ""),
        "title": str(title or ""),
        "start_date": str(start_date or ""),
        "end_date": str(end_date or ""),
        "producer": str(producer or ""),
        "comments": str(comments or ""),
        "mode": str(mode or "Cheer"),
        "team1": (str(team1_no or ""), str(team1_name or "")),
        "team2": (str(team2_no or ""), str(team2_name or ""))
    })

# ------------------------
# INITIALIZE BROWSER
# ------------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(BASE_URL)
wait = WebDriverWait(driver, 15)

# ------------------------
# LOGIN
# ------------------------
print("🔐 Logging in...")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))).send_keys(EMAIL)
driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys(PASSWORD)
driver.find_element(By.XPATH, '//button[text()="LOGIN"]').click()

# Wait for sidebar Events button and click
wait.until(EC.element_to_be_clickable((By.XPATH, '//label[text()="Events"]'))).click()

# Wait until Create Event button is visible (page is loaded)
wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(),"Create Event")]')))

# ------------------------
# CREATE EVENT FUNCTION
# ------------------------
def create_event(data):
    print(f"\n📌 Creating Event: {data['event_code']}")

    # Click + Create Event
    create_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Create Event")]')))
    create_btn.click()

    # Fill Event Code
    code_field = wait.until(EC.presence_of_element_located((By.NAME, "event_code")))
    code_field.clear()
    code_field.send_keys(data["event_code"])

    # Title
    title_field = driver.find_element(By.NAME, "event_title")
    title_field.clear()
    title_field.send_keys(data["title"])

    # Dates
    driver.find_element(By.XPATH, "//input[@placeholder='Start Date']").send_keys(data["start_date"] + Keys.ENTER)
    driver.find_element(By.XPATH, "//input[@placeholder='End Date']").send_keys(data["end_date"] + Keys.ENTER)

    # Producer dropdown
    driver.find_element(By.NAME, "event_producer").click()
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[text()='{data['producer']}']"))).click()

    # Comments
    driver.find_element(By.XPATH, "//textarea[@placeholder='Enter Event Comments']").send_keys(data["comments"])

    # Mode (Cheer / Dance)
    driver.find_element(By.XPATH, f'//label[text()="{data["mode"]}"]').click()

    # Teams
    driver.find_element(By.XPATH, '//button[text()="+ Add Teams"]').click()
    time.sleep(1)
    team1_no, team1_name = data["team1"]
    team2_no, team2_name = data["team2"]

    driver.find_element(By.XPATH, "(//input[@placeholder='Enter team no.'])[1]").send_keys(team1_no)
    driver.find_element(By.XPATH, "(//input[@placeholder='Enter team name'])[1]").send_keys(team1_name + Keys.ENTER)

    driver.find_element(By.XPATH, "(//input[@placeholder='Enter team no.'])[2]").send_keys(team2_no)
    driver.find_element(By.XPATH, "(//input[@placeholder='Enter team name'])[2]").send_keys(team2_name)

    driver.find_element(By.XPATH, '//button[span[text()="Add"]]').click()

    # Toggles (Internet, Onsite Sales, Free)
    for i in range(1, 3+1):
        driver.find_element(By.XPATH, f'(//label[text()="Yes"])[{i}]').click()

    # Status Active
    driver.find_element(By.XPATH, '//label[text()="Active"]').click()

    # Save
    driver.find_element(By.XPATH, '//button[text()="Save"]').click()

    # Verify back on Events page
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(),"Create Event")]')))
    if data["event_code"] in driver.page_source:
        print(f"✅ PASS: Event {data['event_code']} created successfully")
    else:
        print(f"❌ FAIL: Event {data['event_code']} not found after save")

# ------------------------
# RUN EVENTS CREATION
# ------------------------
for case in event_data:
    create_event(case)

print("\n🎉 All events processed!")
time.sleep(3)
driver.quit()