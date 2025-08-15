import logging
import pytest
import time

from selenium.webdriver.common.devtools.v136.dom_storage import clear

from utils.screenshot_utils import capture_full_page_screenshot
from pages.manager_registration_page import ManagerRegistrationPage
from utils.data_loader import load_all_test_data

@pytest.mark.parametrize("test_case",load_all_test_data("../data/data.json"))
def test_tc_mb_man_005(browser_config, test_case):
    logging.info("TC_MB_MAN_005 Started..")
    logging.info(test_case["manager"][4]["TC_MAN_005"]["_comment"])
    driver, wait = browser_config

    # 1. create object for managerPage class
    manager_registration_page = ManagerRegistrationPage(driver,wait)

    # 2. Click on Register As Manager Button
    try:
        manager_registration_page.click_register_as_manager_button()
        logging.info("Register As Manager Button Clicked successfully.")
    except Exception as e:
        logging.error("Element 'Register As Manager' not found with Explicit wait.")
        pytest.fail("Element 'Register As Manager' not found with Explicit wait.")

    time.sleep(3)

    # 3. Enter valid value of Full Name
    try:
        manager_registration_page.enter_manager_fullname(test_case["manager"][4]["TC_MAN_005"]["fullname"])
        logging.info("Valid Full Name Enter successfully.")
    except Exception as e:
        logging.error("Element 'Full Name' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Full Name' not found with Explicit wait. !!!")

    # 4. Enter valid value of Email
    try:
        manager_registration_page.enter_manager_email(test_case["manager"][4]["TC_MAN_005"]["email"])
        logging.info("Valid Email Enter successfully.")
    except Exception as e:
        logging.error("Element 'Email Address' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Email Address' not found with Explicit wait. !!!")

    # 5. Enter invalid (empty) value of Password
    try:
        manager_registration_page.enter_manager_password(test_case["manager"][4]["TC_MAN_005"]["pass"])
        logging.info("Invalid (empty) Password Enter successfully.")
    except Exception as e:
        logging.error("Element 'Password' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Password not found with Explicit wait. !!!")

    # 6. Click on the "Register" button.
    try:
        manager_registration_page.click_manager_register_button()
        logging.info("Click on Register button successfully.")

    except Exception as e:
        logging.error("Element 'Register' button not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Register' button not found with Explicit wait.!!!")

        # Validate Error Message
        expected_error_message = test_case["manager"][4]["TC_MAN_005"]["expected_result"]

        if expected_error_message == manager_registration_page.get_html_popup_error_message("Password"):
            logging.info("Test Passed. Expected Error Message match with Actual Error Message.")

        else:
            logging.error("Test Failed. Expected Error Message does not match with Actual Error Message.")
            pytest.fail("Test Failed. Expected Error Message does not match with Actual Error Message.")
            # Screenshot
            capture_full_page_screenshot(driver, "TC_MB_MAN_005")

        logging.info("TC_MB_MAN_005 Completed..")
