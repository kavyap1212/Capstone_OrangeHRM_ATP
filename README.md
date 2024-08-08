File Structure
conftest.py: Contains configuration and fixtures for setting up and tearing down the test environment.
login_page.py: Defines the LoginPage class representing the login page.
test_tc_pim_01.py: Contains test cases for the "Forgot Password" functionality.
pim_page.py: Defines the PIMPage class representing the PIM page.
test_tc_pim_02.py: Contains test cases for the main menu validation.
test_tc_pim_03.py: Contains test cases for header validation on the Admin page.
Step-by-Step Process to Run Tests
Setup WebDriver:

Ensure the conftest.py file is configured to provide the necessary WebDriver setup and URL.
Create Test Files:

conftest.py: Configures the WebDriver and browser setup.
login_page.py: Contains the LoginPage class with methods to interact with the login page.
pim_page.py: Contains the PIMPage class with methods to interact with the PIM page.
Test Files: Create test cases (test_tc_pim_01.py, test_tc_pim_02.py, test_tc_pim_03.py) with various test scenarios.
Run Tests:

Open a terminal or command prompt.
Navigate to the directory where your test files are located.
Run the tests using bash command: pytest --maxfail=1 --disable-warnings -q

This command will execute the test cases and show results in the terminal.


View HTML Reports: Check the generated HTML report for detailed test results. It is usually saved in the reports directory (specified in pytest.ini or by the pytest command).
