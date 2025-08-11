from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CustomerRegistrationPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def open_your_account_button(self,button):
        account_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, " #homeRegisterCustomerBtnMain")))
        account_button.click()

    def enter_full_name(self, value):
        full_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerNameReg")))
        full_name.send_keys(value)

    def enter_email_address(self, value):
        email_address = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerEmailReg")))
        email_address.send_keys(value)

    def enter_valid_password(self,password):
        valid_password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerPasswordReg")))
        valid_password.send_keys(str(password))

    def enter_initial_deposit(self,initial_deposit):
        promo_code_element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#initialDepositReg")))
        promo_code_element.send_keys(str(initial_deposit))

    def click_register_button(self):
        click_register_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[id='customerRegisterForm'] button[type='submit']")))
        click_register_button.click()

    def expected_successful_message(self):
        actual_successful_message = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#customerRegMessage")))

        return actual_successful_message.text