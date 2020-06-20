import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path='', params=None):
        url = self.base_url + path
        return requests.get(url=url, params=params)

    def post(self, path='', data=None, json=None, headers=None, proxies=None):
        url = self.base_url + path
        return requests.post(url=url, data=data, json=json, headers=headers, proxies=proxies)

    def put(self, path='', data=None, headers=None, proxies=None):
        url = self.base_url + path
        return requests.put(url=url, data=data, headers=headers, proxies=proxies)

    def delete(self, path=''):
        url = self.base_url + path
        return requests.delete(url=url)
