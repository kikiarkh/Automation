import requests
import json
from constans import Base_URL

class Employee:

    def __init__(self, url = Base_URL):
        self.url = url

#Получение списка сотрудников   
    def det_list(self, company_id: int):
        company = {'company': 'company_id'}
        responce = requests.get(self.base_URL+'/employee', params=company)
        return responce.json()

#Добавить нового сотрудника
    def create_new_employee(self, token: str, body: json):
        headers = {'x-client-token': token}
        resp = requests.post(self.url + '/employee',headers=headers, json=body)
        return resp.json()
    
#Получить сотрудника по id
    def get_info(self, employer_id: int):
        resp = requests.get(self.url + '/employee/'+ str(employer_id))
        return resp.json()

#Изменить информацию о сотруднике
    def change_info(self, token: str,  employer_id: int, body: json):
        headers = {'x-client-token': token}
        resp = requests.patch(self.url + '/employee/'+ str(employer_id), headers=headers, json=body)
        return resp.json()

        
        

