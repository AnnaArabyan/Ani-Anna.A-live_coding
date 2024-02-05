import logging
import os
from selenium import webdriver
import pytest
import myconfig

<<<<<<< HEAD
=======
# TODO, remove extra code
# @pytest.fixture()
# def driver():
#     try:
#         options = webdriver.ChromeOptions()
#         options.add_argument('--headless')
#         driver = webdriver.Chrome(options=options)

#         logging.info("The driver is initialized")
#         driver.maximize_window()
#         yield driver
#         driver.quit()
#     except Exception as error:
#         raise Exception(error)

>>>>>>> 7296fef878c39f2000b2417fc1f0e7b6b3a90971
@pytest.fixture()
def driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        logging.info("The driver is initialized")
        driver.maximize_window()
        yield driver
        driver.quit()
    except Exception as error:
        raise Exception(error)

# @pytest.fixture()
# def driver():
#     try:
#         driver = webdriver.Chrome()
#         driver.maximize_window()
#         yield driver
#         driver.quit()
#     except Exception as error:
#         raise Exception(error)   

def pytest_configure():
    logging.basicConfig(
                    level=logging.INFO,
                    filename=os.path.join(os.path.join(os.path.dirname(__file__), myconfig.log_file_name)),
                    filemode='a',
                    encoding='utf-8'
                    )