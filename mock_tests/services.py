import requests
from mock_tests.constants import BASE_URL


def get_images_by_breed(breed: str):
    response = requests.get(BASE_URL + f'breed/{breed}/images')
    if response.ok:
        return response
    else:
        return None


def get_subbreed_list(breed: str):
    response = requests.get(BASE_URL + f'breed/{breed}/list')
    if response.ok:
        return response
    else:
        return None


def get_multiple_random_images(count: int):
    response = requests.get(BASE_URL + f'breeds/image/random/{count}')
    if response.ok:
        return response
    else:
        return None
