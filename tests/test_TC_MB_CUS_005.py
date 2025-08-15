import logging
import pytest
import time

from selenium.webdriver.common.devtools.v136.dom_storage import clear

# from TestCases.TC_TB_02 import expected_error_message
from utils.screenshot_utils import capture_full_page_screenshot
from pages.customer_registration_page import CustomerRegistrationPage
from utils.data_loader import load_booking_test_data

@pytest.mark.parametrize("test_case",load_booking_test_data("../data/data.json"))
def test_tc_mb_cus_005(browser_config, test_case):
    logging.info("TC_MB_CUS_005 Started..")
    logging.info(test_case["customer"][4]["TC_CUS_005"]["_comment"])
    driver, wait = browser_config

    # create object for CustomerPage class
    customer_registration_page = CustomerRegistrationPage(driver,wait)

    # 2. Click on Open Your Account Button
    try:
        customer_registration_page.click_customer_open_account_button()
        logging.info("Open Your Account Button Clicked successfully.")
    except Exception as e:
        logging.error("Element 'Open Your Account Button' not found with Explicit wait.")
        pytest.fail("Element 'Open Your Account Button' not found with Explicit wait.")

    time.sleep(3)

    # 3. Enter valid value of Full Name
    try:
        customer_registration_page.enter_customer_fullname(test_case["customer"][4]["TC_CUS_005"]["fullname"])
        logging.info("Valid Full Name Enter successfully.")
    except Exception as e:
        logging.error("Element 'Full Name' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Full Name' not found with Explicit wait. !!!")

    # 4. Enter valid value of Email
    try:
        customer_registration_page.enter_customer_email(test_case["customer"][4]["TC_CUS_005"]["email"])
        logging.info("Valid Email Enter successfully.")
    except Exception as e:
        logging.error("Element 'Email Address' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Email Address' not found with Explicit wait. !!!")

    # 5. Enter invalid (empty) value of Password
    try:
        customer_registration_page.enter_customer_password(test_case["customer"][4]["TC_CUS_005"]["pass"])
        logging.info("Invalid (empty) Password Enter successfully.")
    except Exception as e:
        logging.error("Element 'Password' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Password not found with Explicit wait. !!!")

    # 6. Enter valid value of Initial Deposit Amount
    try:
        customer_registration_page.enter_customer_ini_deposit(test_case["customer"][4]["TC_CUS_005"]["deposit_amount"])
        logging.info("Valid Initial Deposit Amount Enter successfully.")
    except Exception as e:
        logging.error("Element 'Initial Deposit Amount' not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Initial Deposit Amount' not found with Explicit wait. !!!")


    # 7. Click on the "Register" button.
    try:
        customer_registration_page.click_customer_register_button()
        logging.info("Click on Register button successfully.")

    except Exception as e:
        logging.error("Element 'Register' button not found with Explicit wait.")
        pytest.fail("Test Failed. Element 'Register' button not found with Explicit wait.!!!")


    # Validate Error Message
    expected_error_message = test_case["customer"][4]["TC_CUS_005"]["expected_result"]

    if expected_error_message == customer_registration_page.get_html_popup_error_message("Password"):
        logging.info("Test Passed. Expected Error Message match with Actual Error Message.")

    else:
        logging.error("Test Failed. Expected Error Message does not match with Actual Error Message.")
        pytest.fail("Test Failed. Expected Error Message does not match with Actual Error Message.")
        # Screenshot
        capture_full_page_screenshot(driver, "TC_MB_CUS_005")

    logging.info("TC_MB_CUS_005 Completed..")