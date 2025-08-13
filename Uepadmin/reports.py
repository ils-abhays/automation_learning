import time

from selenium.webdriver.common.by import By

from Uepadmin.config import driver


def reports():
    # from selenium import webdriver
    # from selenium.webdriver.common.by import By
    # import time
    #
    # # Launch browser
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    #
    # # Go to login page
    # driver.get("https://dev-admin.uepviewer.com/")  # Replace with actual login page URL
    # time.sleep(5)
    #
    # # Login
    # driver.find_element(By.XPATH, '//input[@placeholder="Email"]').send_keys("anuuu@gmail.com")
    # driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys("Anee@123")
    # driver.find_element(By.XPATH, '//button[text()="LOGIN"]').click()
    time.sleep(5)

    # Grab and print values one by one
    cards = driver.find_elements(By.CLASS_NAME, "dashboard_report_card")
    total_customers = cards[0].find_element(By.CLASS_NAME, "count_name").text
    total_customerscounts = cards[0].find_element(By.CLASS_NAME, "counts").text
    total_orders = cards[1].find_element(By.CLASS_NAME, "count_name").text
    total_orderscounts =  cards[1].find_element(By.CLASS_NAME, "counts").text
    completed_order = cards[2].find_element(By.CLASS_NAME, "count_name").text
    completed_ordercounts = cards[2].find_element(By.CLASS_NAME, "counts").text
    pending_orders = cards[3].find_element(By.CLASS_NAME, "count_name").text
    pending_orderscounts =  cards[3].find_element(By.CLASS_NAME, "counts").text
    events_created = cards[4].find_element(By.CLASS_NAME, "count_name").text
    events_createdcounts =  cards[4].find_element(By.CLASS_NAME, "counts").text
    # total_orders = driver.find_element(By.XPATH, '//div[contains(text(),"Total Orders")]/preceding-sibling::div').text
    # completed_orders = driver.find_element(By.XPATH, '//div[contains(text(),"Completed Orders")]/preceding-sibling::div').text
    # pending_orders = driver.find_element(By.XPATH, '//div[contains(text(),"Pending Orders")]/preceding-sibling::div').text
    # events_created = driver.find_element(By.XPATH, '//div[contains(text(),"Events Created")]/preceding-sibling::div').text

    # Print results
    print(total_customers + ": " + total_customerscounts)
    print(total_orders + ": " + total_orderscounts)
    print(completed_order + ": " + completed_ordercounts)
    print(pending_orders + ": " + pending_orderscounts)
    print(events_created + ": " + events_createdcounts)

    # Close browser

reports()