from testpage import LoginPage, BlogPage, CreatePostPage, ContactPage
import time

def test_step_error_login(browser, testdata):
    test_login_page = LoginPage(browser, url=testdata['url'])
    test_login_page.goto_site()
    test_login_page.enter_login('test')
    test_login_page.enter_pwd('test')
    test_login_page.click_login_btn()
    assert test_login_page.get_error_login() == '401'

def test_step_login(browser, testdata):
    test_login_page = LoginPage(browser, url=testdata['url'])
    test_login_page.enter_login(testdata['user_data']['username'])
    test_login_page.enter_pwd(testdata['user_data']['password'])
    test_login_page.click_login_btn()
    test_blog_page = BlogPage(test_login_page.driver, test_login_page.base_url)
    username = test_blog_page.get_user_name()
    assert username == f"Hello, {testdata['user_data']['username']}"

def test_step_create_post(browser, testdata):
    test_blog_page = BlogPage(browser, url=testdata['url'])
    test_blog_page.click_add_post()
    test_create_post = CreatePostPage(test_blog_page.driver, test_blog_page.base_url)
    test_create_post.fill_create_post_form()
    test_create_post.submit_create_post_form()
    time.sleep(1)
    name = test_create_post.get_name_created_post()
    test_create_post.delete_created_post()
    time.sleep(1)
    assert name == 'test_text'

def test_step_go_to_contact(browser, testdata):
    test_blog_page = BlogPage(browser, url=testdata['url'])
    test_blog_page.click_contact()
    test_contact_page = ContactPage(test_blog_page.driver, test_blog_page.base_url)
    assert test_contact_page.get_title_contact() == 'Contact us!'

def test_step_fill_contact_form(browser, testdata):
    test_contact_page = ContactPage(browser, url=testdata['url'])
    test_contact_page.fill_contact_form()
    form_data = test_contact_page.get_form_data()
    assert form_data == ['test', 'test@mail.com', 'test']

def test_step_contact_alert(browser, testdata):
    test_contact_page = ContactPage(browser, url=testdata['url'])
    test_contact_page.click_contact_us()
    alert_text = test_contact_page.get_alert_text()
    assert alert_text == 'Form successfully submitted'