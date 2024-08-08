from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  # You can adjust the timeout value as needed

    # Locator for the 'Admin' menu item
    admin_menu_locator = (By.XPATH, '//span[text()="Admin"]')
    
    # Add other locators as needed

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            raise Exception(f"Element not found: {locator}. Error: {e}")

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_menu_item(self, item_name):
        # Define locators for each menu item based on the item name
        return (By.XPATH, f'//span[text()="{item_name}"]')

    # Add methods to interact with different elements on the PIM page
    def click_admin_menu(self):
        self.click_element(self.admin_menu_locator)

    def is_menu_item_visible(self, item_name):
        menu_item_locator = self.get_menu_item(item_name)
        try:
            menu_element = self.find_element(menu_item_locator)
            return menu_element.is_displayed()
        except Exception:
            return False