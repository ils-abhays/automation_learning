from Uepadmin.config import driver


def Files():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time

    # # Setup Chrome options
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Prevent extra blank tab
    # options.add_argument("--disable-blink-features=AutomationControlled")       # Optional: cleaner launch
    #
    # # Launch browser
    # driver = webdriver.Chrome(options=options)
    # driver.get("https://dev-admin.uepviewer.com/")
    # time.sleep(5)
    #
    # # Login
    # driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys("anuuu@gmail.com")
    # driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("Anee@123")
    # driver.find_element(By.XPATH, '//button[text()="LOGIN"]').click()
    time.sleep(5)

    # Go to Files
    driver.find_element(By.XPATH, '//label[text()="Files"]').click()

    # Search
    search_input = driver.find_element(By.NAME, "eventSearchParam")
    search_input.send_keys("MD2024")
    search_input.send_keys(Keys.ENTER)

    print("✅ Script completed. Browser is still open.")


Files()
