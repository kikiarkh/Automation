import requests
import json
from constans import Base_URL

class Company:
    
    def __init__(self, url = Base_URL):
        self.url = url

    def get_company(self, token: str, body: json):
        headers = {'x-client-token': token}
        resp = requests.patch(self.url + '/company', headers=headers, params=body)
        return resp.json()
    
    def last_active_company(self):
        active_params = {
            'active': 'true'
        }
        resp = requests.get(self.url + '/company', params=active_params)
        return resp.json()[-1]['id']
    