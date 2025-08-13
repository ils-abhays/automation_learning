Automation Project (Selenium + Python)
Files included:

config.py : driver setup and configuration (update chromedriver path)
utils.py : reusable wait/click/type helpers
base_page.py : base page class used by page objects
login_page.py : login page object
forgot_password_page.py : forgot password page object
dashboard_page.py : simple dashboard actions
main_test.py : example test flow
requirements.txt : python dependencies
How to use:

Update C_PATH in config.py to point to your chromedriver executable.
(Optional) Update BASE_URL, USERNAME, PASSWORD in config.py.
Create virtual environment and install dependencies: python -m venv .venv ..venv\Scripts\activate pip install -r requirements.txt
Run main_test.py: python main_test.py
Note: The example main_test.py uses placeholders; update credentials or calls as required.
