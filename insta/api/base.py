from insta.config.loader import get_token, get_endpoint
import requests
import json


class BaseAPI(object):
    def __init__(self, http_method):
        self._token = get_token()
        self._params = {
            "access_token": self._token
        }
        self._base_endpoint = get_endpoint()
        self.req_method = requests.get if http_method is "GET" else requests.post


    def request(self, uri, extra_params):
        params = {**self._params, **extra_params}
        req = self.req_method(self._base_endpoint + uri, params=params)
        return json.loads(req.text)