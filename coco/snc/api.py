import time
import requests


class AbstractApi:
    """
        Abstract Api class
    """
    default_kwargs = {}
    last_request = 0
    request_rate = 1

    def __init__(self, **kwargs):
        """
        :param kwargs: default arguments for API
        """
        self.cfg = {k: kwargs.get(k, self.default_kwargs[k]) for k in self.default_kwargs}

    def _request(self, url, params=None, http_method='GET'):
        """
        Ordinary request
        :param url: requested url
        :param params: params for request
        :param http_method: HTTP method of request
        :return: response as dict (deserialized json)
        """

        time_diff = time.time() - self.last_request
        if time_diff < self.request_rate:
            time.sleep(self.request_rate - time_diff)
        self.last_request = time.time()

        if http_method == 'GET':
            request = requests.get
        elif http_method == 'POST':
            request = requests.post
        else:
            raise ValueError('Unallowed HTTP method "{}"'.format(http_method))
        res = request(url, params=params)
        if res.ok:
            return res.json()
        else:
            return {'error': {'error_code': -1, 'error_msg': 'http error'}}
