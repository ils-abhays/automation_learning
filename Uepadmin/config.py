from selenium import webdriver
from selenium.webdriver.common.keys import Keys
c_path = r"E:\PycharmProjects\chromedriver-win64\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=c_path)
from selenium.webdriver.chrome.service import Service as ChromeService

# Create a FirefoxService object to start the Firefox driver
chrome_service = ChromeService(executable_path=c_path)

# Create a Firefox driver using the service
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()
url = "https://dev-admin.uepviewer.com/"