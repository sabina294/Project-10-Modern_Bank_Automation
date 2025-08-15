import logging
import pytest
import time

from selenium.webdriver.common.devtools.v136.dom_storage import clear

from utils.screenshot_utils import capture_full_page_screenshot
from pages.manager_registration_page import ManagerRegistrationPage
from utils.data_loader import load_booking_test_data

@pytest.mark.parametrize("test_case",load_booking_test_data("../data/data.json"))
def test_tc_mb_man_001(browser_config, test_case):
    logging.info("TC_MB_MAN_001 Started..")
    logging.info(test_case["manager"][0]["TC_MAN_001"]["_comment"])
    driver, wait = browser_config

    # 1.create object for ManagerPage class
    manager_registration_page = ManagerRegistrationPage(driver,wait)

    # 2. Click on Register As Manager Button
    try:
        manager_registration_page.click_register_as_manager_button()
        logging.info("Register As Manager Button Clicked successfully.")
    except Exception as e:
        logging.error("Element 'Register As Manager Button' not found with Explicit wait.")
        pytest.fail("Element 'Register As Manager Button not found with Explicit wait.")

    time.sleep(2)
    # 3. Enter EMPTY value of Full Name
    try:
        manager_registration_page.enter_manager_fullname(test_case["manager"][0]["TC_MAN_001"]["fullname"])
        logging.info("Empty Full Name Enter successfully.")
    except Exception as e:
        logging.error("Element 'Full Name' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Full Name' not found with Explicit wait. !!!")

    # 4. Enter valid value of Email
    try:
        manager_registration_page.enter_manager_email(test_case["manager"][0]["TC_MAN_001"]["email"])
        logging.info("Valid Email Enter successfully.")
    except Exception as e:
        logging.error("Element 'Email Address' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Email Address' not found with Explicit wait. !!!")

    # 5. Enter valid value of Password
    try:
        manager_registration_page.enter_manager_password(test_case["manager"][0]["TC_MAN_001"]["pass"])
        logging.info("Valid Password Enter successfully.")
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
    expected_error_message = test_case["manager"][0]["TC_MAN_001"]["expected_result"]

    if expected_error_message == manager_registration_page.get_html_popup_error_message("FullName"):
        logging.info("Test Passed. Expected Error Message match with Actual Error Message.")

    else:
        logging.error("Test Failed. Expected Error Message does not match with Actual Error Message.")
        pytest.fail("Test Failed. Expected Error Message does not match with Actual Error Message.")
        # Screenshot
        capture_full_page_screenshot(driver, "TC_MB_MAN_001")

    logging.info("TC_MB_MAN_001 Completed..")