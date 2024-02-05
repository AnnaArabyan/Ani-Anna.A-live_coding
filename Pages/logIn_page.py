from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
import myconfig

class LogIn(Helper):
    input_email = (By.XPATH, '//input[@id="ap_email"]')
    input_password = (By.XPATH, '//input[@id="ap_password"]')
    btn_click = (By.XPATH, '//input[@id="signInSubmit"]')
    

    def LogIn(self):
        self.find_and_send_keys(self.input_email, myconfig.email)
        self.find_and_send_keys(self.input_password, myconfig.password)
        self.find_and_click(self.btn_click)
      