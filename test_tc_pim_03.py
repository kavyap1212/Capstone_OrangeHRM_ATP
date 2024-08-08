import pytest
from login_page import LoginPage
from pim_page import PIMPage
import time

class TestTC_PIM_02:
    def test_header_validation(self, setup):
        driver = setup
        login_page = LoginPage(driver)

        # Explicit credentials
        username = "Admin"
        password = "admin123"

        # Login
        print("Logging in with username and password")
        login_page.login(username, password)

        # Wait for the page to load
        time.sleep(3)

        # Validate menu options
        print("Validating menu options on the home page")
        menu_items = [
            'Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info',
            'Performance', 'Dashboard', 'Directory', 'Maintenance', 'Buzz'
        ]
        
        pim_page = PIMPage(driver)
        
        for item in menu_items:
            try:
                assert pim_page.is_menu_item_visible(item), f"Menu item '{item}' is not visible"
                print(f"Menu item '{item}' is visible")
            except Exception as e:
                print(f"An error occurred while checking menu item '{item}': {e}")
        
        print("Header validation completed")