from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# App Config - update BASE_URL, C_PATH, USERNAME, PASSWORD as required
BASE_URL = "https://dev-admin.uepviewer.com/"
USERNAME = "anuuu@gmail.com"
PASSWORD = "Anee@123"

# Path to your chromedriver executable - update this to your local path
C_PATH = r"E:\PycharmProjects\chromedriver-win64\chromedriver.exe"

def get_driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # Keep browser open
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--start-maximized")
    service = Service(C_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
