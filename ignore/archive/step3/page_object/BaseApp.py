from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import logging

class BasePage:
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.base_url = url
        
    def find_element(self, locator, time=10):
        ignored_exceptions=(NoSuchElementException, StaleElementReferenceException)
        try:
            
            element = WebDriverWait(self.driver, time, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located(locator),
            message=f"Cant't find element by locator {locator}" 
            )
        except Exception as e:
            logging.exception(e)
        logging.info(f'Element found')
        return element
    
    def find_elements(self, locator, time=10):
        ignored_exceptions=(NoSuchElementException, StaleElementReferenceException)
        try:
            
            element = WebDriverWait(self.driver, time, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Cant't find element by locator {locator}" 
            )
        except Exception as e:
            logging.exception(e)
        logging.info(f'Element found')
        return element
    
    def switch_to_alert(self, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
            EC.alert_is_present(),
            message=f"Alert is not present" 
            )
        except Exception as e:
            logging.exception(e)
        logging.info(f'Switch to alert')
        return element
    
    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        logging.info(f'Element property{property} get')
        return element.value_of_css_property(property)
    
    def goto_site(self):
        self.driver.get(self.base_url)
        logging.info(f'Url {self.base_url} get')