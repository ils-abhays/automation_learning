from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ✅ Correct path to chromedriver.exe
service = Service(r"E:\PycharmProjects\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.google.com")

# Keep the browser open for a while
input("Press Enter to close the browser...")

# Close browser
driver.quit()
