import requests
import yaml
with open('config.yaml') as f:
    load_data = yaml.safe_load(f)


def auth_user(load_data):
    user = load_data['user_data']
    url = load_data['url_gb'] + 'gateway/login'
    res = requests.post(url=url, data=user)
    token = res.json()['token']
    id = res.json()['id']
    username = res.json()['username']
    print(username)
    headers = {'X-Auth-Token': token}
    url1 = load_data['url_gb'] + 'api/posts'
    data = {'title': 'test1', 'description': 'test_description1', 'content': 'test_content1'}
    res1 = requests.post(url=url1, data=data, headers=headers)
    print(res1.json())
    params ={'username': username}
    print(username)
    print(headers)
    response = requests.get(url=url1, params=params, headers=headers)
    print(response.json())
    return headers, id, username

if __name__ == '__main__':
    print(auth_user(load_data))
