from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper
import random
import logging
import time
class DataHandling(Helper):
        
<<<<<<< HEAD
    search_result = (By.XPATH, '//a[@class="Wm-z"]')

    Chloe = (By.XPATH, '//a[@class="FE-z" and span="Chloe"]')
    GUESS = (By.XPATH, '//a[@class="FE-z" and span="GUESS"]')
    Lacoste = (By.XPATH, '//a[@class="FE-z" and span="Lacoste"]')
    Nike_Kids = (By.XPATH, '//a[@class="FE-z" and span="Nike Kids"]')
    PSD = (By.XPATH, '//a[@class="FE-z" and span="PSD"]')
    RAEN_Optics = (By.XPATH, '//a[@class="FE-z" and span="RAEN Optics"]')
    Ray_Ban = (By.XPATH, '//a[@class="FE-z" and span="Ray-Ban"]')
    ro_sham_bo_baby = (By.XPATH, '//a[@class="FE-z" and span="ro.sham.bo baby"]')
    Royal_Robbins = (By.XPATH, '//a[@class="FE-z" and span="Royal Robbins"]')
    Timberland = (By.XPATH, '//a[@class="FE-z" and span="Timberland"]')
=======
    search_result = (By.XPATH, '//a[@class="Vr-z"]')
    # TODO, no need to keep all brand and colors locators, instead get locators to all elements under brand and use random.choice to click on random checkbox
    Chloe = (By.XPATH, '//a[@class="sF-z" and span="Chloe"]')
    GUESS = (By.XPATH, '//a[@class="sF-z" and span="GUESS"]')
    Lacoste = (By.XPATH, '//a[@class="sF-z" and span="Lacoste"]')
    Nike_Kids = (By.XPATH, '//a[@class="sF-z" and span="Nike Kids"]')
    PSD = (By.XPATH, '//a[@class="sF-z" and span="PSD"]')
    RAEN_Optics = (By.XPATH, '//a[@class="sF-z" and span="RAEN Optics"]')
    Ray_Ban = (By.XPATH, '//a[@class="sF-z" and span="Ray-Ban"]')
    ro_sham_bo_baby = (By.XPATH, '//a[@class="sF-z" and span="ro.sham.bo baby"]')
    Royal_Robbins = (By.XPATH, '//a[@class="sF-z" and span="Royal Robbins"]')
    Timberland = (By.XPATH, '//a[@class="sF-z" and span="Timberland"]')
>>>>>>> 7296fef878c39f2000b2417fc1f0e7b6b3a90971

    brand_list = [Chloe,GUESS, Lacoste, Nike_Kids, PSD, RAEN_Optics, Ray_Ban, ro_sham_bo_baby, Royal_Robbins, Timberland]

    ten_and_under = (By.XPATH, '//a[@class="FE-z" and span="$10.00 and Under"]')
    twenty_five_and_under = (By.XPATH, '//a[@class="FE-z" and span="$25.00 and Under"]')
    thirty_and_under = (By.XPATH, '//a[@class="FE-z" and span="$30.00 and Under"]')
    thirty_five_and_under = (By.XPATH, '//a[@class="FE-z" and span="$35.00 and Under"]')
    forty_and_under = (By.XPATH, '//a[@class="FE-z" and span="$40.00 and Under"]')
    fifty_and_under = (By.XPATH, '//a[@class="FE-z" and span="$50.00 and Under"]')
    sixty_and_under = (By.XPATH, '//a[@class="FE-z" and span="$60.00 and Under"]')
    seventy_and_under  = (By.XPATH, '//a[@class="FE-z" and span="$70.00 and Under"]')
    seventy_five_and_under = (By.XPATH, '//a[@class="FE-z" and span="$75.00 and Under"]')
    hundred_and_under = (By.XPATH, '//a[@class="FE-z" and span="$100.00 and Under"]')
    two_hundred_and_under = (By.XPATH, '//a[@class="FE-z" and span="$200.00 and Under"]')
    two_hundred_and_over = (By.XPATH, '//a[@class="FE-z" and span="$200.00 and Over"]')

    price_list = [ten_and_under, twenty_five_and_under, thirty_and_under, thirty_five_and_under, forty_and_under,
                  fifty_and_under, sixty_and_under, seventy_and_under, seventy_five_and_under, hundred_and_under,
                  two_hundred_and_under, two_hundred_and_over]

    
    blue = (By.XPATH, '//a[@class="FE-z" and span="Blue"]')
    multi = (By.XPATH, '//a[@class="FE-z" and span="Multi"]')
    beige = (By.XPATH, '//a[@class="FE-z" and span="Beige"]')
    gray = (By.XPATH, '//a[@class="FE-z" and span="Gray"]')
    red = (By.XPATH, '//a[@class="FE-z" and span="Red"]')
    black = (By.XPATH, '//a[@class="FE-z" and span="Black"]')
    brown = (By.XPATH, '//a[@class="FE-z" and span="Brown"]')
    burgundy = (By.XPATH, '//a[@class="FE-z" and span="Burgundy"]')
    gold = (By.XPATH, '//a[@class="FE-z" and span="Gold"]')
    khaki = (By.XPATH, '//a[@class="FE-z" and span="Khaki"]')
    pink = (By.XPATH, '//a[@class="FE-z" and span="Pink"]')
    silver = (By.XPATH, '//a[@class="FE-z" and span="Silver"]')

    color_list = [blue, multi, beige, gray, red, black, brown, burgundy, gold, khaki, pink, silver]

    expected_brand = (By.XPATH, '//dd[@class="Zm-z"]/span[@itemprop="name"]')
    expected_price = (By.XPATH, '//dd[@class="_m-z"]/span[@itemprop="price"]')
    expected_color = (By.XPATH, '//dd[@class="pla-z" and @itemprop="color"]')


    def search_not_empty(self):
        self.element_count(self.search_result)

    # def search_for_brand_random(self):
    #     self.random_brand_locator = random.choice(self.brand_list)
    #     self.find_and_click(self.random_brand_locator)
        
    def search_for_brand_random(self):
        self.random_brand_locator = random.choice(self.brand_list)
        self.find_and_click(self.random_brand_locator)
        selected_element_brand = self.browser.find_element(*self.random_brand_locator)
        element_text = selected_element_brand.text
        logging.info(f"Text brand value of the selected element: {element_text}")
        return element_text

        
    # def search_for_price_random(self):
    #     random_price_locator = random.choice(self.price_list)
    #     self.find_elem_ui_and_click(random_price_locator)
        
    def search_for_price_random(self):
        random_price_locator = random.choice(self.price_list)
        self.find_elem_ui_and_click(random_price_locator)
        selected_element_price = self.browser.find_element(*random_price_locator)
        element_text_price = selected_element_price.text
        logging.info(f"Text price value of the selected element: {element_text_price}")
        return element_text_price

    
    # def search_for_color_random(self):
    #     random_color_locator = random.choice(self.color_list)
    #     self.find_elem_ui_and_click(random_color_locator)

    def search_for_color_random(self):
        random_color_locator = random.choice(self.color_list)
        self.find_elem_ui_and_click(random_color_locator)
        selected_element_color = self.browser.find_element(*random_color_locator)
        element_text_color = selected_element_color.text
        logging.info(f"Text color value of the selected element: {element_text_color}")
        return element_text_color

        

    def compare_results(self):
        element_text = self.search_for_brand_random()
        element_text_price = self.search_for_price_random()
        element_text_color = self.search_for_color_random()

        expected_brand_element = self.browser.find_element(*self.expected_brand)
        expected_brand_text = expected_brand_element.text
        assert element_text == expected_brand_text, f"Brand text mismatch: Expected '{expected_brand_text}'"

        expected_price_element = self.browser.find_element(*self.expected_price)
        expected_price_text = expected_price_element.text
        assert element_text_price == expected_price_text, f"Brand text mismatch: Expected '{expected_price_text}'"

        expected_color_element = self.browser.find_element(*self.expected_color)
        expected_color_text = expected_color_element.text
        assert element_text_color == expected_color_text, f"Brand text mismatch: Expected '{expected_color_text}'"






    
        
        
