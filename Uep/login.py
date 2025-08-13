from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ------------------------
# CONFIGURATION
# ------------------------
BASE_URL = "https://dev-admin.uepviewer.com/"

# Test data: (email, password, expected_result)
login_test_cases = [
    ("validuser@example.com", "wrongpass", "fail"),
    ("invaliduser@example.com", "somepass", "fail"),
    ("invaliduser", "somepass", "fail"),
    ("", "password123", "fail"),
    ("validuser@example.com", "", "fail"),
("anuuu@gmail.com", "Anee@1234", "fail"),
("anuuuaa@gmail.com", "Anee@123", "fail"),
    ("anuuu@gmail.com", "Anee@123", "success")
]

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
    time.sleep(1)  # Let page load

    # Enter email
    email_field = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Email"]'))
    )
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
    toast_text = None
    try:
        toast = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast-body"))
        )
        toast_text = toast.text
    except:
        pass
    finally:
        if toast_text:  # Only print if toast is found
            print(f"🔔 Toast Message: {toast_text}")

    # ------------------------
    # CHECK FIELD VALIDATION MESSAGES
    # ------------------------
    validation_texts = []
    try:
        validation_msgs = WebDriverWait(driver, 2).until(
            EC.presence_of_all_elements_located((
                By.XPATH, '//form[contains(@class,"login_form")]//div[contains(@class,"text-danger")]'
            ))
        )
        for msg in validation_msgs:
            text = msg.text.strip()
            if text:
                validation_texts.append(text)
    except:
        pass
    finally:
        for text in validation_texts:
            print(f"⚠️ Field Validation: {text}")

    # ------------------------
    # CHECK RESULTS
    # ------------------------
    # ------------------------
    # CHECK RESULTS
    # ------------------------
    if expected == "success":
        try:
            # Wait for "Reports" heading after successful login
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//h3[@class="heading_report" and text()="Reports"]')
                )
            )
            print("✅ PASS: Login successful")
        except:
            print("❌ FAIL: Login failed, expected success")
    else:
        # For failure cases, check for any toast or validation message first
        page_source_lower = driver.page_source.lower()
        if "error" in page_source_lower or "invalid" in page_source_lower:
            print("✅ PASS: Error message displayed for invalid login")

# ------------------------
# CLOSE BROWSER
# ------------------------
driver.quit()
