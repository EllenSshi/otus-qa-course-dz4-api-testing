import pytest
from apiclient.api_client import APIClient


@pytest.mark.withparams
def test_status_for_url(url, status_code):
    api_client = APIClient(url)
    resp = api_client.get()
    assert resp.status_code == status_code
