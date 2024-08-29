import pytest
import requests
import logging


@pytest.fixture()
def auth_user(load_data):
    '''Authorization user and get auth-x token for test'''
    user = load_data['user_data']
    url = load_data['url_gb'] + 'gateway/login'
    try:
        res = requests.post(url=url, data=user)
    except:
        logging.exception(f'Request url {url} with user {user} not successful ')
    if not res:
        logging.error(f'Request auth url {url} user {user} is empty')
        return False
    token = res.json()['token']
    id = res.json()['id']
    username = res.json()['username']
    headers = {'X-Auth-Token': token}
    if not all([id , username, token]):
        logging.error(f'id {id} or username {username} or token {token} is empty')
        return False
    return headers, id, username

@pytest.fixture
def notMe(load_data):
    '''Set test data from config.yaml'''
    return load_data['url_gb'], load_data['url_posts'], load_data['notme']

@pytest.fixture
def test_text(load_data):
    '''Set text for test'''
    return load_data['test']

@pytest.fixture
def post_data(load_data):
    '''Set test data from config.yaml'''
    data = {'title': 'test1', 'description': 'test_description1', 'content': 'test_content1'}
    url = load_data['url_gb'] + load_data['url_posts']
    return url, data

@pytest.fixture
def create_post(auth_user, post_data):
    '''Get description of post from request api, for testing'''
    headers, *_ = auth_user
    url, data = post_data
    try:
        response = requests.post(url=url, data=data, headers=headers)
    except:
        logging.exception(f'Request for url {url} with data {data} and headers {headers} not successful')
        return False
    if not ('<Response [200]>' in str(response)):
        logging.error(f'Request for url {url} with data {data} and headers {headers} return wrong response {response}')
        return False
    return data['description']

@pytest.fixture
def get_posts(auth_user, post_data):
    '''Get post data json from request api for testing'''
    headers, _, username = auth_user
    url, _ = post_data
    params ={'username': username}
    try:
        posts = requests.get(url=url, params=params, headers=headers).json()
    except:
        logging.exception(f'Request for url {url} with params {params} and headers {headers} not successful')
        return False
    if not posts:
        logging.error(f'Request for url {url} with data {data} and headers {headers} return empty posts {posts}')
        return False
    return posts['data']


