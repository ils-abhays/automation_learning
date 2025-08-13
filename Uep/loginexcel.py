from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

# ------------------------
# CONFIGURATION
# ------------------------
BASE_URL = "https://dev-admin.uepviewer.com/"
EXCEL_FILE = r"E:\PycharmProjects\PythonProject2\login_test_data.xlsx" # Path to your Excel file

# ------------------------
# READ TEST CASES FROM EXCEL
# ------------------------
workbook = openpyxl.load_workbook(EXCEL_FILE)
sheet = workbook.active

login_test_cases = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    email, password, expected = row
    login_test_cases.append((str(email or ""), str(password or ""), str(expected or "").lower()))

# ------------------------
# INITIALIZE BROWSER
# ------------------------
driver = webdriver.Chrome()
driver.maximize_window()

# ------------------------
# RUN TEST CASES
# ------------------------
for email, password, expected in login_test_cases:
    print(f"\n--- Testing Email: '{email}' | Password: '{password}' ---")

    driver.get(BASE_URL)
    time.sleep(1)

    # Enter email
    email_field = driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
    email_field.clear()
    email_field.send_keys(email)

    # Enter password
    password_field = driver.find_element(By.XPATH, '//input[@placeholder="Password"]')
    password_field.clear()
    password_field.send_keys(password)

    # Click LOGIN button
    driver.find_element(By.XPATH, '//button[text()="LOGIN"]').click()

    # ------------------------
    # CHECK TOAST MESSAGE
    # ------------------------
    try:
        toast = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast-body"))
        )
        if toast.text.strip():
            print(f"🔔 Toast Message: {toast.text}")
    except:
        pass  # Skip if no toast is displayed

    # ------------------------
    # CHECK FIELD VALIDATION MESSAGES
    # ------------------------
    try:
        validation_msgs = WebDriverWait(driver, 1).until(
            EC.presence_of_all_elements_located((
                By.XPATH, '//form[contains(@class,"login_form")]//div[contains(@class,"text-danger")]'
            ))
        )
        found_validation = False
        for msg in validation_msgs:
            text = msg.text.strip()
            if text:
                print(f"⚠️ Field Validation: {text}")
                found_validation = True
        if not found_validation:
            pass  # Skip printing "No validation message"
    except:
        pass

    # ------------------------
    # CHECK RESULTS
    # ------------------------
    if expected == "success":
        try:
            WebDriverWait(driver, 8).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//h3[@class="heading_report" and text()="Reports"]')
                )
            )
            print("✅ PASS: Login successful")
        except:
            print("❌ FAIL: Login failed, expected success")
    else:
        if "error" in driver.page_source.lower() or "invalid" in driver.page_source.lower():
            print("✅ PASS: Error message displayed for invalid login")
        else:
            print("❌ FAIL: No error message, expected failure")

# ------------------------
# CLOSE BROWSER
# ------------------------
driver.quit()
