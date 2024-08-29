import pytest
import requests

@pytest.fixture
def coord():
    return '37.7891838', '-122.4033522'

@pytest.fixture
def text():
    return 'One MNontgomery Tower'

@pytest.fixture()
def auth_user(load_data):
    user = load_data['user_data']
    url = load_data['url_gb'] + 'gateway/login'
    res = requests.post(url=url, data=user)
    token = res.json()['token']
    id = res.json()['id']
    username = res.json()['username']
    headers = {'X-Auth-Token': token}
    return headers, id, username

@pytest.fixture
def notMe(load_data):
    return load_data['url_gb'], load_data['url_posts'], load_data['notme']

@pytest.fixture
def test_text():
    return '9ttddf'

@pytest.fixture
def post_data(load_data):
    data = {'title': 'test1', 'description': 'test_description1', 'content': 'test_content1'}
    url = load_data['url_gb'] + load_data['url_posts']
    return url, data

@pytest.fixture
def create_post(auth_user, post_data):
    headers, *_ = auth_user
    url, data = post_data
    requests.post(url=url, data=data, headers=headers)
    return data['description']

@pytest.fixture
def get_posts(auth_user, post_data):
    headers, _, username = auth_user
    url, _ = post_data
    params ={'username': username}
    posts = requests.get(url=url, params=params, headers=headers).json()
    return posts['data']


