import logging
import datetime
from Pages.header import Header
from Pages.logIn_page import LogIn
from Pages.search_page import DataHandling
from Helpers.general_helpers import Helper
import myconfig
import time


# TODO, change test name, its not a runner
def test_info_search(driver):
    logging.info("Start_time: %s", datetime.datetime.now())

    helper_obj = Helper(driver)
    helper_obj.go_to_page(myconfig.url)

    header_obj = Header(driver)
    header_obj.signIn()

    time.sleep(5)
    login_page_obj = LogIn(driver)
    login_page_obj.LogIn()

    time.sleep(5)
    header_obj.item_search()

    search_page_obj = DataHandling(driver)
    search_page_obj.search_not_empty()
    time.sleep(5)
    search_page_obj.search_for_brand_random()
    time.sleep(5)
    search_page_obj.search_for_price_random()
    time.sleep(5)
    search_page_obj.search_for_color_random()
    time.sleep(5)


    logging.info("End_time: %s", datetime.datetime.now())

    


   
   
    
   
  


    
    
 