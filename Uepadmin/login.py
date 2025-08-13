from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
from config import driver

# Open the website
config.driver.get(config.url)  # Replace with the URL of the website you want to log in to
config.driver.maximize_window()
email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
email_field.send_keys("anuuu@gmail.com")  # Replace with test email

# Step 3: Enter password
password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password_field.send_keys("Anee@123")  # Replace with test password

# Step 4: Optionally click "Remember me"
remember_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
remember_checkbox.click()

# Step 5: Click Login button
login_button = driver.find_element(By.XPATH, "//button[text()='LOGIN']")
login_button.click()

# Wait for some time to let the next page load
# time.sleep(5)
driver.implicitly_wait(10)
# Optional: Validate login success (depends on URL or element after login)
print("Page Title After Login:", driver.title)
# Close the browser
# driver.quit()

















# # Find the username and password input fields and enter your credentials
# username_field = driver.find_element (By.ID, "//input[@placeholder='anuuu@gmail.com']")  # Replace with the actual ID of the username input field
# password_field = config.driver.find_element(By.ID, "//input[@placeholder='Password']")  # Replace with the actual ID of the password input field
# login = config.driver.find_element(By.ID, "//button[text()='LOGIN']")
# username_field.send_keys("anuuu@gmail.com")
# password_field.send_keys("Anee@123")
# driver.implicitly_wait(10)
# # Submit the form
# password_field.send_keys(Keys.RETURN)
#
# # You might need to add some waiting here to make sure the next page loads properly
# # For example, you can use driver.implicitly_wait(10) to wait for up to 10 seconds
#
# # Now you should be logged in and can perform further actions on the website
# # For example, you can navigate to different pages, scrape data, or interact with elements
# # Remember to close the browser when you're done
# config.driver.close()
