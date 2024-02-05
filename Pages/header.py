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
        #TODO, add logging here, try except handdling

<<<<<<< HEAD
    def hover_to_accessories(self):
        self.hover_to_element(self.btn_accessories)

    def accessories_click(self):
        self.find_and_click(self.watches)


        

    
=======
    def item_search(self):
        self.find_and_send_keys(self.input_search_field, data.search_text)
        self.find_and_click(self.btn_search)
        #TODO, add logging here
>>>>>>> 7296fef878c39f2000b2417fc1f0e7b6b3a90971
      



    
        


        