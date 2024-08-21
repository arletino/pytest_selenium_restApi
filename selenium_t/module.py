import yaml
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



with open('./config.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


class Site:
    def __init__(self, address):
        match browser:
            case 'firefox':
                service = Service(executable_path=GeckoDriverManager().install())
                options = webdriver.FirefoxOptions()
                self.driver = webdriver.Firefox(service=service, options=options)
            case 'chrome':
                service = Service(executable_path=ChromeDriverManager().install())
                options = webdriver.ChromeOptions()
                self.driver = webdriver.Chrome(service=service, options=options)
            case 'edge':
                service = Service(executable_path=EdgeChromiumDriverManager().install())
                options = webdriver.EdgeOptions()
                self.driver = webdriver.Edge(service=service, options=options)
            case _:
                raise TypeError
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(address)

    def find_element(self, mode, path):
        time.sleep(testdata['sleep_time'])
        match mode:
            case 'css':
                type_sel = By.CSS_SELECTOR
            case 'xpath':
                type_sel =By.XPATH
            case _:
                element = None
        
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((type_sel, path))) 
        return element[0]
    
    def get_element_property(self, mode, path, property):
        # time.sleep(testdata['sleep_time'])
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)
    
    def quit(self):
        time.sleep(testdata['sleep_time'])
        self.driver.close()


class Chrome:
    def __init__(self, address) :
        service = Service(testdata['driver_chrome'])
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get(address)
        # time.sleep(testdata['sleep_time'])

class Gecko:
    def __init__(self, address):
        service = Service(testdata['driver_gecko'])
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get(address)
        # time.sleep(testdata['sleep_time'])

class Edge:
    def __init__(self, address):
        service = Service(testdata['driver_edge'])
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get(address)
        # time.sleep(testdata['sleep_time'])
