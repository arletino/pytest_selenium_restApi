import pytest
import yaml


@pytest.fixture
def test_data(config_file='./config.yaml'):
    with open(config_file) as f:
        return yaml.safe_load(f)
    
@pytest.fixture
def sl_login():
    return  '''//*[@id="login"]/div[1]/label/input'''

@pytest.fixture
def sl_pwd():
    return  '''//*[@id="login"]/div[2]/label/input'''

@pytest.fixture
def sl_error():
    return  '''//*[@id="app"]/main/div/div/div[2]/h2'''

@pytest.fixture
def sl_btn():
    return 'button'

@pytest.fixture
def error_txt():
    return '401'

@pytest.fixture
def get_username(test_data):
    return f'Hello, {test_data["user_data"]["username"]}'


@pytest.fixture
def btn_create_post():
    return '''//*[@id="create-btn"]'''

@pytest.fixture
def title_in():
    return '''//*[@id="create-item"]/div/div/div[1]/div/label/input'''

@pytest.fixture
def description_in():
    return '''//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'''

@pytest.fixture
def content_in():
    return '''//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'''

@pytest.fixture
def btn_save():
    return '''//*[@id="create-item"]/div/div/div[7]/div/button'''

@pytest.fixture
def sl_post_name():
    return '''/html/body/div[1]/main/div/div[1]/h1'''
    