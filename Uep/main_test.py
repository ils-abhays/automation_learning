from config import get_driver
from login_page import LoginPage
from dashboard_page import DashboardPage
import time

driver = get_driver()

# Login flow
login_page = LoginPage(driver)
login_page.open()
login_page.login("anuuu@gmail.com", "Anee@123")
time.sleep(3)

# Dashboard actions (example)
dashboard = DashboardPage(driver)
# dashboard.logout()  # Uncomment to logout at the end
print('Demo flow completed.')
