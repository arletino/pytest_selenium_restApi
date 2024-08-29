import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope='session', autouse=True)
def testdata():
    with open('./config.yaml') as f:
        return  yaml.safe_load(f)

# @pytest.fixture(scope='session')
def data_locators():
    with open('./page_object/locators.yaml') as f:
        data = yaml.safe_load(f)
    return {
    name:(type_locator, value )
    for type_locator, locator in data.items() 
    for name, value in locator.items()
    }

        

@pytest.fixture(scope='session')
def browser(testdata):
    browser = testdata['browser']
    match browser:
        case 'firefox':
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(service=service, options=options)
        case 'chrome':
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome(service=service, options=options)
        case 'edge':
            service = Service(executable_path=EdgeChromiumDriverManager().install())
            options = webdriver.EdgeOptions()
            driver = webdriver.Edge(service=service, options=options)
        case _:
            raise TypeError
    yield driver
    driver.quit()