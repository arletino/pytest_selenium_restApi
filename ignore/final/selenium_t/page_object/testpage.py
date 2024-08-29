from BaseApp import BasePage
import logging
from locators import TestSearchLocators

class Service:
    def input_text_into_field(self, word, locator, description=None):
        if not description:
            description = locator
        text_field = self.find_element(locator)
        if not text_field:
            logging.error(f'Element {description} not found')
            return False
        try:
            text_field.clear()
            text_field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {description}')
            return False
        logging.debug(f'Element {description} found')
        return True
    
    def click_btn(self, locator, description=None):
        if not description:
            description = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            self.find_element(locator).click()
        except:
            logging.exception(f'Exception with click button {description}')
            return False
        logging.debug(f'Clicked by {description} button')
        return True
    
    def get_text_form_element(self, locator, description=None):
        if not description:
            description = locator
        element = self.find_element(locator, time=3)
        if not element:
            return None
        try:
            text = element.text
        except:
            logging.exception(f'Exception while get test from {description}')
        logging.debug(f'We fing text {text} in element {description}')
        return text
    
    def fill_form(self, word, locator, description=None):
        if not description:
            description = locator
        form_fields = self.find_elements(locator)
        if not form_fields:
            logging.error(f'Element {description} not found')
            return False
        try:
            for field in form_fields:
                field.clear()
                if (field.get_attribute('type') in ('text',  'textarea')):
                    field.send_keys(word)
                elif field.get_property('type') == 'email':
                    field.send_keys(f"{word}@mail.com")
        except:
            logging.exception(f'Exception while operation with {description}')
            return False
        logging.debug(f'Element {description} fill')
        return True    
    
    def submit_form(self, locator, description=None):
        if not description:
            description = locator
        form_button = self.find_element(locator)
        if not form_button:
            return False
        try:
            self.find_element(locator).submit()
        except:
            logging.exception(f'Exception with submit form {description}')
            return False
        logging.debug(f'Form {description} submit')
        return True
    
    def get_data_form(self, locator, description=None):
        if not description:
            description = locator
        form_fields = self.find_elements(locator)
        if not form_fields:
            logging.error(f'Element {description} not found')
            return False
        try:
            data = [field.get_attribute('value') for field in form_fields]
        except:
            logging.exception(f'Exception while operation with {description}')
            return False
        logging.debug(f'Data from form {description} get')
        return data
    
    def get_alert_text(self,description=None):
        if not description:
            description = "Some Alert"
        alert = self.switch_to_alert()
        if not alert:
            logging.error(f'Alert {description} not found')
            return False
        try:
            text = alert.text
        except:
            logging.exception(f'Exception while operation with {description}')
            return False
        logging.debug(f'Text from alert {description} get')
        return text
        
        

class LoginPage(BasePage):

    service = Service
 
    def enter_login(self, word):
        self.service.input_text_into_field(
            self, 
            word, 
            TestSearchLocators.LOCATOR_LOGIN, 
            description="Login"
            )
    
    def enter_pwd(self, word):
        self.service.input_text_into_field(
            self,
            word, 
            TestSearchLocators.LOCATOR_PWD, 
            description="Login"
            )
    
    def click_login_btn(self):
        self.service.click_btn(
            self,
            TestSearchLocators.LOCATOR_LOGIN_BTN, 
            description='Login'
            )
        
    def get_error_login(self):
        error_text = self.service.get_text_form_element(
            self, 
            TestSearchLocators.LOCATOR_ERROR_FIELD, 
            description='Login'
            )
        return error_text

class BlogPage(BasePage):

    service = Service

    def get_user_name(self):
        username = self.service.get_text_form_element(
            self, 
            TestSearchLocators.LOCATOR_BLOG_USERNAME, 
            description='Username after login'
            )
        return username 
       
    def click_contact(self):
        self.service.click_btn(
            self, 
            TestSearchLocators.LOCATOR_BLOG_CONTACT_HREF, 
            description='Contact href'
            )
    
    def click_add_post(self):
        self.service.click_btn(
            self, 
            TestSearchLocators.LOCATOR_BLOG_BTN_ADD_POST, 
            description='Button Add post'
            )

class CreatePostPage(BasePage):
    service = Service 

    def fill_create_post_form(self):
        self.service.fill_form(
            self, 
            'test_text', 
            TestSearchLocators.LOCATOR_CONTACT_FORM, 
            description='Fill post form'
            )
    
    def submit_create_post_form(self):
        self.service.submit_form(
            self, 
            TestSearchLocators.LOCATOR_CREATE_POST_FORM_BTN,
            description='Submit post form'
            )
    
    def get_name_created_post(self):
        post_name = self.service.get_text_form_element(
            self,
            TestSearchLocators.LOCATOR_CREATED_POST_NAME,
            description='Get name created post'
            )
        return post_name
    
    def delete_created_post(self):
        self.service.click_btn(
            self, 
            TestSearchLocators.LOCATOR_DELETE_CREATED_POST,
            description='Delete created post'
            )

class ContactPage(BasePage):
    service = Service

    def fill_contact_form(self):
        self.service.fill_form(
            self, 
            'test', 
            TestSearchLocators.LOCATOR_CONTACT_FORM, 
            description='Fill contact form'
            )

    def get_title_contact(self):
        title = self.service.get_text_form_element(
            self, 
            TestSearchLocators.LOCATOR_CONTACT_FORM_TITLE,
            description='Get title of contact form'
            )
        return title

    def get_form_data(self):
        data = self.service.get_data_form(
            self, 
            TestSearchLocators.LOCATOR_CONTACT_FORM, 
            description='Get data from contact form'
            )
        return data

    
    def click_contact_us(self):
        self.service.submit_form(
            self, 
            TestSearchLocators.LOCATOR_CONTACT_BTN_CONTACTUS, 
            description='Submit contact form "contact us"'
            )

    
    def get_alert_text(self):
        return self.service.get_alert_text(self)
    