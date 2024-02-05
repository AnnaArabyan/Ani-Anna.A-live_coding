from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
from TestData import data

class Header(Helper):
    btn_login = (By.XPATH, '//div[@class="x-z"]//a[@class="F-z"]')
    input_search_field = (By.XPATH, '//input[@id="searchAll"]')
    btn_search = (By.XPATH, '//button[@class="D-z"]')
    btn_accessories = (By.XPATH, '//a[@href="/accessories"]')
    watches = (By.XPATH, '//a[@href="/watches/CLHXAeICAQE.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/"]')
    
    def signIn(self):
        self.find_and_click(self.btn_login)

    def hover_to_accessories(self):
        self.hover_to_element(self.btn_accessories)

    def accessories_click(self):
        self.find_and_click(self.watches)


        

    
      



    
        


        