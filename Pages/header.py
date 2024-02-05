from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
from TestData import data



class Header(Helper):
    btn_login = (By.XPATH, '//div[@class="z-z"]//a[@class="H-z"]')
    input_search_field = (By.XPATH, '//input[@id="searchAll"]')
    btn_search = (By.XPATH, '//button[@class="F-z"]')
    
    def signIn(self):
        self.find_and_click(self.btn_login)
        #TODO, add logging here, try except handdling

    def item_search(self):
        self.find_and_send_keys(self.input_search_field, data.search_text)
        self.find_and_click(self.btn_search)
        #TODO, add logging here
      



    
        


        