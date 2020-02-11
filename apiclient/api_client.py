import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path='', params=None):
        url = self.base_url + path
        return requests.get(url=url, params=params)

    def post(self, path='', params=None, data=None, headers=None, proxies=None):
        url = self.base_url + path
        return requests.post(url=url, params=params, data=data, headers=headers, proxies=proxies)
