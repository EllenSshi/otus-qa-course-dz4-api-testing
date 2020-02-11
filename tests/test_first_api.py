import pytest
import requests
from apiclient.api_client import APIClient


base_url = 'https://dog.ceo/api/'
api_client = APIClient(base_url)


@pytest.mark.parametrize("rand_count, expected_count", [(3, 3), (5, 5), (51, 50)])
def test_multiple_random_images_count(rand_count, expected_count):
    """
    Проверка, что api вернул столько имеджей, сколько мы попросили. Не возвращает более 50 имеджей.
    """
    resp = api_client.get(f'breeds/image/random/{rand_count}')
    assert len(resp.json()['message']) == expected_count


@pytest.mark.parametrize("breed_name, expected_status_code, expected_status_text",
                         [('labrador', 200, 'success'), ('boxer', 200, 'success'),
                          ('corgi', 200, 'success'), ('corgashik', 404, 'error')])
def test_search_images_by_breed(breed_name, expected_status_code, expected_status_text):
    """
    Проверка наличия имеджей определенных пород.
    """
    resp = api_client.get(f'breed/{breed_name}/images')
    assert resp.status_code == expected_status_code
    assert resp.json()['status'] == expected_status_text


def test_
