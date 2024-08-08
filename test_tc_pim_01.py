import pytest
from login_page import LoginPage
from selenium.webdriver.common.by import By
import time

class TestTC_PIM_01:
    def test_forgot_password(self, setup):
        driver = setup
        login_page = LoginPage(driver)

        # Click on the "Forgot your password?" link
        login_page.click_forgot_password()

        # Wait for the password reset page to load
        time.sleep(2)

        # Enter username and click on Reset Password
        login_page.reset_password('Admin')
        
        # Wait for the action to complete
        time.sleep(2)
        
        # Add assertions here if needed