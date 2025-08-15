import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome() # Or any other browser driver


driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 20)
print("starting .....")
driver.get("https://muntasir101.github.io/Modern-Bank-Portal/")

# print("gone to the URL")
#
#
# time.sleep(5)
# print("5 sec past")
try:
    print("In try sec")
    Customer_go_reg_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#homeRegisterCustomerBtnMain")))
    Customer_go_reg_button.click()
    print("Successful: Clicked on Customer_go_reg_button")
except Exception as e:
    print(e)

# time.sleep(3)
error_message=''

# Locate the required textbox
try:
    fullname_textbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,  "#customerNameReg")))

    fullname_textbox.send_keys("Tareq Hassan")

    # Attempt to submit the form without entering text (to trigger validation)
    # This depends on your form's submission mechanism (e.g., clicking a submit button)
    submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,  "form[id='customerRegisterForm'] button[type='submit']")))
    submit_button.click()
    time.sleep(10)
    # Wait for the error message to appear (if it's dynamically loaded)
    # Consider using explicit waits for better reliability

    # Retrieve the error message text
    # For HTML5 validation message:
    error_message = fullname_textbox.get_attribute("validationMessage")

    # For a custom error message element (if present in the DOM):
    # error_message_element = driver.find_element(By.CSS_SELECTOR, ".error-message-class")
    # error_message = error_message_element.text
except Exception as e:
    print(e)

# Assert the error message
expected_message = "Please fill out this field!!!." # Or your custom expected message
# if error_message == expected_message :
print(f"Expected: '{expected_message}', Got: '{error_message}'")

driver.quit()