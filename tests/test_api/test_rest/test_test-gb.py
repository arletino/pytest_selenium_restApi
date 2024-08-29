import pytest
import requests

@pytest.mark.rest
def test_get_posts_notme(auth_user, test_text, notMe):
    headers, *_ = auth_user
    url_gb, url_post, notme = notMe
    response = requests.get(url_gb + url_post, params=notme, headers=headers)
    listres = [i['title'] for i in response.json()['data']]
    assert test_text in listres

@pytest.mark.rest
def test_create_post(create_post, get_posts) :
    description = create_post
    posts = get_posts
    res = [post for post in posts if post['description'] == description]
    assert res