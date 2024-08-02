import requests
import pytest
import json
from Employee import Employee
from Company import Company

company = Company()
employee = Employee()

def test_auth(get_token):
    token = get_token
    assert token is not None

def test_company_id():
    company_id = company.last_active_company()
    assert company_id is not None

def test_new_employer(get_token):
    token = str(get_token)
    
    company_id = company.last_active_company()
    new_employer = {
            "id": 0,
            "firstName": "Ekaterina",
            "lastName": "Rybakova",
            "middleName": "Nikolayevna",
            "companyId": company_id,
            "email": "kat@gmail.com",
            "url": 'string',
            "phone": "string",
            "birthdate": "2024-08-02T13:49:14.712Z",
            "isActive": True
        }
    new_employer_id = (employee.get_new(token, new_employer))['id']
    assert new_employer_id is not None

def test_get_info(get_token):
    token = str(get_token)

    company_id = company.last_active_company()
    new_employer = {
            "id": 0,
            "firstName": "Ekaterina",
            "lastName": "Rybakova",
            "middleName": "Nikolayevna",
            "companyId": company_id,
            "email": "kat@gmail.com",
            "url": 'string',
            "phone": "string",
            "birthdate": "2024-08-02T13:49:14.712Z",
            "isActive": True
        }
    new_employer_id = (employee.get_new(token, new_employer))['id']
    
    info_employer = employee.get_info(new_employer_id)
    assert new_employer['id'] == info_employer['id']

def change_employer_info(get_token):
    token = get_token
    
    company_id = company.last_active_company()
    body_employer = {
            "id": 0,
            "firstName": "Ekaterina",
            "lastName": "Rybakova",
            "middleName": "Nikolayevna",
            "companyId": company_id,
            "email": "kat@gmail.com",
            "url": 'string',
            "phone": "string",
            "birthdate": "2024-08-02T13:49:14.712Z",
            "isActive": True
        }
    just_employer = employee.get_new(body_change)
    id = just_employer['id']
    body_change = {
        "lastName": "Change",
        "email": "test@gmail.com",
        "url": "string",
        "phone": "string",
        "isActive": True
        }
    employer_change = employee.change_info()
    assert employer_change.status_code == 200
    assert id == employer_change.json()['id']








    


