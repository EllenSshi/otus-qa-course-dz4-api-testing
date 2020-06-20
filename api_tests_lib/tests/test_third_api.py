import pytest
import random
from apiclient.api_client import APIClient
from jsonschema import validate


base_url = 'https://jsonplaceholder.typicode.com/'
api_client = APIClient(base_url)


@pytest.mark.parametrize("post_id, new_title, new_body, user_id",
                         [(1, 'This is new title', 'This is new body', '1'),
                          (11, 'Some new title', 'Some new body', '2'),
                          (21, 'Looks like new title', 'Looks like new body', '3')])
def test_update_post(post_id, new_title, new_body, user_id):
    body = {
        'title': new_title,
        'body': new_body,
        'userId': user_id
    }
    resp = api_client.put(f'posts/{post_id}', data=body)
    assert resp.json()['id'] == post_id
    assert resp.json()['title'] == new_title
    assert resp.json()['body'] == new_body
    assert resp.json()['userId'] == user_id


def test_delete_random_post():
    random_post_id = random.randint(1, 100)
    resp = api_client.delete(f'posts/{random_post_id}')
    assert resp.status_code == 200


@pytest.mark.parametrize("album_id", [5, 35, 44, 87])
def test_get_album_id_photos(album_id):
    resp = api_client.get('photos', params={'albumId': album_id})
    assert resp.status_code == 200
    assert resp.json()[random.randint(0, len(resp.json()))]['albumId'] == album_id


def test_todos_list_validation():
    resp = api_client.get('todos')
    schema = {
        'type': 'array',
        'uniqueItems': True,
        'items': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer', 'minimum': 1},
                'userId': {'type': 'integer', 'minimum': 1},
                'title': {'type': 'string'},
                'completes': {'type': 'boolean'}
            },
            "required": ['id', 'userId', 'title', 'completed']
        }
    }
    validate(instance=resp.json(), schema=schema)


def test_get_photos_response_time():
    """
    Проверка, что время ответа на запрос списка всех фото не превышает 0.5 секунды.
    """
    resp = api_client.get('photos')
    assert resp.elapsed.microseconds < 500000
