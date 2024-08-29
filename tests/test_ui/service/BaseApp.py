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
            return None
        logging.debug(f'Element found')
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
        logging.debug(f'Element found')
        return element
    
    def switch_to_alert(self, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
            EC.alert_is_present(),
            message=f"Alert is not present" 
            )
        except Exception as e:
            logging.exception(e)
            return None
        logging.debug(f'Switch to alert')
        return element
    
    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if not element:
            logging.error(f'Property {property} not found with locator {locator}')
        else:
            logging.debug(f'Property{property} get with locator {locator}')
        return element.value_of_css_property(property)
    
    def goto_site(self):
        try:
            goto_url = self.driver.get(self.base_url)
            logging.debug(f'Url {self.base_url} is load')
        except:
            logging.exception("Exception wile open url")
            goto_url = None
        return goto_url