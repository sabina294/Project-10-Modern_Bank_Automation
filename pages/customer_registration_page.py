from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class CustomerRegistrationPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def click_customer_open_account_button(self):
        customer_open_account_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#homeRegisterCustomerBtnMain")))
        customer_open_account_button.click()

    def enter_customer_fullname(self, customer_fullname_value):
        customer_fullname = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerNameReg")))
        customer_fullname.send_keys(str(customer_fullname_value))

    def enter_customer_email(self, customer_email_value):
        customer_fullname = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerEmailReg")))
        customer_fullname.send_keys(str(customer_email_value))

    def enter_customer_password(self, customer_password_value):
        customer_password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerPasswordReg")))
        customer_password.send_keys(str(customer_password_value))

    def enter_customer_ini_deposit(self, customer_ini_deposit_value):
        customer_ini_deposit = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#initialDepositReg")))
        customer_ini_deposit.send_keys(str(customer_ini_deposit_value))

    def click_customer_register_button(self):
        customer_register_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[id='customerRegisterForm'] button[type='submit']")))
        customer_register_button.click()

    def get_final_price(self):
        actual_final_price_element = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(6) > strong:nth-child(6)")))

        return actual_final_price_element.text

    def get_html_popup_error_message(self,form_field_name):
        form_field_css_id= ''
        if 'FullName' == form_field_name :
            form_field_css_id = "#customerNameReg"
        elif 'Email' == form_field_name :
            form_field_css_id = "#customerEmailReg"
        elif 'Password' == form_field_name :
            form_field_css_id = "#customerPasswordReg"
        elif 'InitialDeposit' == form_field_name :
            form_field_css_id = "#initialDepositReg"

        form_field_error_element = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, form_field_css_id)))

        return form_field_error_element.get_attribute("validationMessage")

    def get_customer_reg_message(self):

        customer_Reg_Message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#customerRegMessage')))

        return customer_Reg_Message.text

    # customerRegMessage