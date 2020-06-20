import pytest
import random
from apiclient.api_client import APIClient
from jsonschema import validate


base_url = 'https://api.openbrewerydb.org/breweries/'
api_client = APIClient(base_url)


def test_random_brewery_id():
    random_brewery_id = random.randint(1, 8029)
    resp = api_client.get(f'{random_brewery_id}')
    assert resp.json()['id'] == random_brewery_id


def test_breweries_list_jsonschema_validation():
    resp = api_client.get('')
    schema = {
        'type': 'array',
        'uniqueItems': True,
        'items': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer', 'minimum': 1},
                'name': {'type': 'string'},
                'brewery_type': {'type': 'string',
                                 'enum': ['micro', 'regional', 'brewpub', 'large', 'planning', 'bar', 'contract', 'proprietor']
                                 },
                'street': {'type': 'string'},
                'city': {'type': 'string'},
                'state': {'type': 'string'},
                'postal_code': {'type': 'string'},
                'country': {'type': 'string'},
                'longitude': {'type': 'string'},
                'latitude': {'type': 'string'},
                'phone': {'type': 'string'},
                'website_url': {'type': 'string'},
                'updated_at': {'type': 'string'},
                'tag_list': {'type': 'array'}
            },
            "required": ['id', 'name']
        }
    }
    validate(instance=resp.json(), schema=schema)


@pytest.mark.parametrize("count", [5, 25, 50])
def test_breweries_per_page_filter(count):
    resp = api_client.get('', params={'per_page': count})
    assert len(resp.json()) == count


@pytest.mark.parametrize("brewery_name", ['dog', 'california', 'modern', 'times'])
def test_breweries_filter_by_name_count(brewery_name):
    resp_with_filter = api_client.get('', params={'by_name': brewery_name})
    assert len(resp_with_filter.json()) > 0


def test_sorted_by_id_breweries():
    resp = api_client.get('', params={'sort': 'id'})
    list_of_ids = []
    for item in resp.json():
        list_of_ids.append(item['id'])
    assert sorted(list_of_ids) == list_of_ids
