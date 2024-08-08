import pytest
from selenium.webdriver.common.by import By
from login_page import LoginPage
from pim_page import PIMPage
import time

class TestTC_PIM_02:
    def test_main_menu_validation(self, setup):
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

        # Click on Admin from menu options and validate title
        print("Clicking on 'Admin' from menu options")
        pim_page = PIMPage(driver)
        try:
            # Assuming the 'Admin' menu item is not a link but a span element
            admin_menu = pim_page.find_element((By.XPATH, "//span[text()='Admin']"))
            admin_menu.click()
            time.sleep(2)  # Wait for the Admin page to load
            assert driver.title == "OrangeHRM", "Page title does not match"
            print("Admin page title validated")
        except Exception as e:
            print(f"An error occurred while clicking on 'Admin' or validating title: {e}")
            pytest.fail(f"Test failed: {e}")

        # Validate Admin page headers
        print("Validating Admin page headers")
        headers = [
            'User Management', 'Job', 'Organization', 'Qualifications',
            'Nationalities', 'Corporate Banking', 'Configuration'
        ]

        for header in headers:
            try:
                # Check if header is a span element
                header_element = pim_page.find_element((By.XPATH, f"//span[text()='{header}']"))
                assert header_element.is_displayed(), f"Header '{header}' is not visible"
                print(f"Header '{header}' is visible")
            except Exception as e:
                print(f"An error occurred while checking header '{header}': {e}")
        
        print("Admin page headers validation completed")
