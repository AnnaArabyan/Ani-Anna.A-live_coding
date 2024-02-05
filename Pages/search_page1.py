from selenium.webdriver.common.by import By
from Helpers.general_helpers import Helper

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import logging
import time
class DataHandling(Helper):
        
    search_result = (By.XPATH, '//a[@class="Wm-z"]')
    
    brands_list_locator = (By.XPATH, '//ul[@aria-labelledby="brandNameFacet"]')
    brand_links_locator = (By.CLASS_NAME, 'FE-z')

    prices_list_locator = (By.XPATH, '//ul[@aria-labelledby="priceFacet"]')
    price_links_locator = (By.CLASS_NAME, 'FE-z')

    color_list_locator = (By.XPATH, '//ul[@aria-labelledby="colorFacet"]')
    color_links_locator = (By.CLASS_NAME, 'FE-z')


    expected_brand = (By.XPATH, '//dd[@class="Zm-z"]/span[@itemprop="name"]')
    expected_price = (By.XPATH, '//dd[@class="_m-z"]/span[@itemprop="price"]')
    expected_color = (By.XPATH, '//dd[@class="pla-z" and @itemprop="color"]')


    def search_not_empty(self):
        self.element_count(self.search_result)

    def search_for_brand_random(self):

        brands_div = self.browser.find_element(*self.brands_list_locator)
        brand_links = brands_div.find_elements(*self.brand_links_locator)
        random_brand_link = random.choice(brand_links)
        brand_name = random_brand_link.find_element(By.TAG_NAME, 'span').text
        self.find_and_click(self.brand_links_locator)
        logging.info(f"Text brand value of the selected element: {brand_name}")
        return brand_name
    

    def search_for_price_random(self):
        prices_div = self.browser.find_element(*self.prices_list_locator)
        price_links = prices_div.find_elements(*self.price_links_locator)
        random_price_link = random.choice(price_links)
        price_text = random_price_link.find_element(By.TAG_NAME, 'span').text
        self.find_elem_ui_and_click(self.price_links_locator)
        logging.info(f"Text price value of the selected element: {price_text}")
        return price_text
    
    def search_for_color_random(self):
        colors_ul = self.browser.find_element(*self.color_list_locator)
        color_links = colors_ul.find_elements(*self.color_links_locator)
        random_color_link = random.choice(color_links)
        color_text = random_color_link.find_element(By.TAG_NAME, 'span').text
        self.find_elem_ui_and_click(random_color_link)
        logging.info(f"Text color value of the selected element: {color_text}")
        return color_text
    
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