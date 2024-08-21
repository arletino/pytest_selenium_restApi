from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import logging
import time

class TestSearchLocators:
    LOCATOR_LOGIN =(By.XPATH, '''//*[@id="login"]/div[1]/label/input''')
    LOCATOR_PWD =(By.XPATH, '''//*[@id="login"]/div[2]/label/input''')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '''//*[@id="app"]/main/div/div/div[2]/h2''')
    LOCATOR_BLOG_USERNAME = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[3]/a''')
    LOCATOR_BLOG_CONTACT_HREF = (By.XPATH, '''//*[@id="app"]/main/nav/ul/li[2]/a''')
    LOCATOR_BLOG_BTN_ADD_POST = (By.XPATH, '''//*[@id="create-btn"]''')
    LOCATOR_CREATE_POST_FORM = (By.CLASS_NAME, '''"mdc-text-field__input"''')
    LOCATOR_CREATE_POST_FORM_BTN = (By.XPATH ,'''//*[@id="create-item"]/div/div/div[7]/div/button''')
    LOCATOR_CREATED_POST_NAME = (By.XPATH, '''//*[@id="app"]/main/div/div[1]/h1''')
    LOCATOR_DELETE_CREATED_POST = (By.XPATH, '''//*[@id="app"]/main/div/div[1]/div/div[1]/div[1]/button[2]''')
    LOCATOR_CONTACT_NAMEFIELD = (By.XPATH, '''//*[@id="contact"]/div[1]/label/input''')
    LOCATOR_CONTACT_EMAILFIELD = (By.XPATH, '''//*[@id="contact"]/div[2]/label/input''')
    LOCATOR_CONTACT_CONTENTLFIELD = (By.XPATH, '''//*[@id="contact"]/div[3]/label/input''')
    LOCATOR_CONTACT_BTN_CONTACTUS = (By.XPATH, '''//*[@id="contact"]/div[4]/button/span''')
    LOCATOR_CONTACT_FORM = (By.CLASS_NAME, '''mdc-text-field__input''')
    LOCATOR_CONTACT_FORM_TITLE = (By.XPATH, '''//*[@id="app"]/main/div/div/h1''')

class LoginPage(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN)
        login_field.clear()
        login_field.send_keys(word)
        logging.info(f'Enter {word} in to logging field')
    
    def enter_pwd(self, word):
        pwd_field = self.find_element(TestSearchLocators.LOCATOR_PWD)
        pwd_field.clear()
        pwd_field.send_keys(word)
        logging.info(f'Enter {word} in to password field')
    
    def click_login_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
        logging.info(f'Click by logging button')
    def get_error_login(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3).text
        logging.info(f'Get error text - {error_field}')
        return error_field

class BlogPage(BasePage):
    def get_user_name(self):
        username = self.find_element(TestSearchLocators.LOCATOR_BLOG_USERNAME).text
        logging.info(f'Get username {username} after logging')
        return username    
    def click_contact(self):
        self.find_element(TestSearchLocators.LOCATOR_BLOG_CONTACT_HREF).click()
        logging.info(f'Click on href "Contact"')
    
    def click_add_post(self):
        self.find_element(TestSearchLocators.LOCATOR_BLOG_BTN_ADD_POST).click()

class CreatePostPage(BasePage):

    def fill_create_post_form(self):
        create_post_form = self.find_elements(TestSearchLocators.LOCATOR_CONTACT_FORM)
        for field in create_post_form:
            print(field.get_attribute('type'))
            if field.get_attribute('type') == 'text' or field.get_attribute('type') == 'textarea':
                field.send_keys("just some random text")
    
    def submit_create_post_form(self):
        create_post_btn = self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_FORM_BTN).click()
    
    def get_name_created_post(self):
        post_name = self.find_element(TestSearchLocators.LOCATOR_CREATED_POST_NAME)
        return post_name.text
    
    def delete_created_post(self):
        self.find_element(TestSearchLocators.LOCATOR_DELETE_CREATED_POST).click()

class ContactPage(BasePage):

    def fill_contact_form(self):
        contactform = self.find_elements(TestSearchLocators.LOCATOR_CONTACT_FORM)
        for field in contactform:
            if field.get_property('type') == 'email':
                field.send_keys("test@test.com")    
            else:
                field.send_keys("test")

    def get_title_contact(self):
        return self.find_element(TestSearchLocators.LOCATOR_CONTACT_FORM_TITLE).text

    def get_form_data(self):
        contactform = self.find_elements(TestSearchLocators.LOCATOR_CONTACT_FORM)
        return [field.get_attribute('value') for field in contactform]

    def get_name_field(self, name):
        namefield = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAMEFIELD)
        namefield.clear()
        namefield.send_keys(name)
        logging.info(f'Fill field Name {name}')

    def get_email_field(self, email):
        emailfield = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAILFIELD)
        emailfield.clear()
        emailfield.send_keys(email)
        logging.info(f'Fill field Email {email}')
    
    def get_content_field(self, content):
        contentfield = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENTLFIELD)
        contentfield.clear()
        contentfield.send_keys(content)
        logging.info(f'Get field Content {content}')
    
    def click_contact_us(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN_CONTACTUS).submit()
        logging.info(f'Click on btn "Contact Us"')
    
    def get_alert_text(self):
        try:
            alert = self.switch_to_alert()
        except NoAlertPresentException: 
            return False
        return alert.text


    