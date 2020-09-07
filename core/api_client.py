import requests
import json
from core.data_parser import data_parser

class ApiClient:

    def _get_json(self, url):
        response = requests.get(url)
        json_data = json.loads(response.text)
        assert 200 == response.status_code
        return json_data

    def get_link(self, url, field_name):
        json = self._get_json(url)
        return data_parser(json, field_name)
