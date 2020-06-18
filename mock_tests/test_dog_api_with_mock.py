from mock_tests.services import get_images_by_breed, get_subbreed_list, get_multiple_random_images
from unittest.mock import Mock, patch


@patch('mock_tests.services.requests.get')
def test_get_images_by_breed(mock_get):
    """
    Проверка наличия имеджей определенных пород.
    """
    mock_get.return_value.ok = True
    response = get_images_by_breed('corgii')
    assert response is not None


# точно такой же тест как выше, но упадет, потому уходит реальый запрос и сервис отвечает ошибкой (без mock)
def test_get_images_by_breed2():
    """
    Проверка наличия имеджей определенных пород.
    """
    response = get_images_by_breed('corgii')
    assert response is not None


def test_get_subbreed_list():
    with patch('mock_tests.services.requests.get') as mock_get:
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = {
            'message': ["huskysubbreed1", "huskysubbreed2", "huskysubbreed3"],
            'status': 'success'
        }
        response = get_subbreed_list('husky')
        assert bool(response.json()['message'])


def test_get_multiple_random_images():
    with patch('mock_tests.services.requests.get') as mock_get:
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = {
            'message': ["https://images.dog.ceo/breeds/terrier-border/n02093754_1652.jpg"],
            'status': 'success'
        }
        count = 1
        response = get_multiple_random_images(count)
        assert len(response.json()['message']) == count
