import pytest

@pytest.fixture
def set_urlsoap(load_data):
    return load_data['url_soap']

@pytest.fixture
def set_words():
    check_words = ['Привет', 'Прювет']
    return check_words