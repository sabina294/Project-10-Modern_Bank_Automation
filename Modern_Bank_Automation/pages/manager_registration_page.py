from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ManagerRegistrationPage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

    def click_register_as_manager_button(self):
        register_as_manager_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#homeRegisterManagerBtn")))
        register_as_manager_button.click()

    def enter_manager_fullname(self, manager_fullname_value):
        manager_fullname = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#managerNameReg")))
        manager_fullname.send_keys(str(manager_fullname_value))

    def enter_manager_email(self, manager_email_value):
        manager_email = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#managerEmailReg")))
        manager_email.send_keys(str(manager_email_value))


    def enter_manager_password(self, manager_password_value):
        manager_password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#managerPasswordReg")))
        manager_password.send_keys(str(manager_password_value))

    def click_manager_register_button(self):
        manager_register_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[id='managerRegisterForm'] button[type='submit']")))
        manager_register_button.click()

    def get_final_price(self):
        actual_final_price_element = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(6) > strong:nth-child(6)")))

        return actual_final_price_element.text

    def get_html_popup_error_message(self, form_field_name):
        form_field_css_id = ''
        if 'FullName' == form_field_name:
            form_field_css_id = "#managerNameReg"
        elif 'Email' == form_field_name:
            form_field_css_id = "#managerEmailReg"
        elif 'Password' == form_field_name:
            form_field_css_id = "#managerPasswordReg"

        form_field_error_element = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, form_field_css_id)))

        return form_field_error_element.get_attribute("validationMessage")

    def get_manager_reg_message(self):

        manager_reg_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#managerRegMessage')))

        return manager_reg_message.text

    # managerRegMessage




