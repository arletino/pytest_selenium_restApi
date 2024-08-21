import pytest
from module import Site


def test_error_login(test_data, sl_login, sl_pwd, sl_btn, sl_error, error_txt):
    site = Site(test_data['address'])
    login_field = site.find_element('xpath', sl_login)
    login_field.send_keys('test')
    pwd_field = site.find_element('xpath', sl_pwd)
    pwd_field.send_keys('test')
    btn = site.find_element('css', sl_btn)
    btn.click()
    error = site.find_element('xpath', sl_error).text
    site.quit()
    assert error == error_txt

def test_login(test_data, sl_login, sl_pwd, sl_btn, get_username):
    site = Site(test_data['address'])
    login_field = site.find_element('xpath', sl_login)
    login_field.clear()
    login_field.send_keys(test_data['user_data']['username'])
    pwd_field = site.find_element('xpath', sl_pwd)
    pwd_field.clear()
    pwd_field.send_keys(test_data['user_data']['password'])
    btn = site.find_element('css', sl_btn)
    btn.click()
    sl_hello = '''/html/body/div[1]/main/nav/ul/li[3]/a'''
    username = site.find_element('xpath', sl_hello).text
    site.quit()
    assert username == get_username

def test_create_post(test_data, 
                sl_login, 
                sl_pwd, 
                sl_btn, 
                btn_create_post, 
                title_in, 
                description_in, 
                content_in, 
                btn_save,
                sl_post_name
                ):
    site = Site(test_data['address'])
    login_field = site.find_element('xpath', sl_login)
    login_field.clear()
    login_field.send_keys(test_data['user_data']['username'])
    pwd_field = site.find_element('xpath', sl_pwd)
    pwd_field.clear()
    pwd_field.send_keys(test_data['user_data']['password'])
    btn = site.find_element('css', sl_btn)
    btn.click()
    btn_post = site.find_element('xpath', btn_create_post)
    btn_post.click()
    title_field = site.find_element('xpath', title_in)
    title_field.clear()
    title = 'test_checking'
    title_field.send_keys(title)
    desc_field = site.find_element('xpath', description_in)
    desc_field.clear()
    desc = 'description checking'
    desc_field.send_keys(desc)
    content_field = site.find_element('xpath', content_in)
    content_field.clear()
    content = 'content checking'
    content_field.send_keys(content)
    btn_sv = site.find_element('xpath', btn_save)
    btn_sv.click()
    post_name = site.find_element('xpath', sl_post_name).text
    site.quit()
    assert post_name == title
