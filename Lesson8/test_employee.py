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

def test_create_new_employer(get_token):
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
    new_employer_id = (employee.create_new_employee(token, new_employer))['id']
    assert new_employer_id is not None

def test_create_new_employer_without_token():
    company_id = company.last_active_company()
    token = ""
    body_employer = {
            "id": 0,
            "firstName": "Elena",
            "lastName": "Ivanova",
            "middleName": "Nikolayevna",
            "companyId": company_id,
            "email": "test@gmail.com",
            "url": 'string',
            "phone": "string",
            "birthdate": "2024-08-02T13:49:14.712Z",
            "isActive": True
        }
    new_employer = employee.create_new_employee(token, body_employer)
    assert new_employer['message'] == "Unauthorized"

def test_create_new_employer_without_body(get_token):
    token = str(get_token)
    
    company_id = company.last_active_company()
    body_employer = {}
    new_employer = employee.create_new_employee(token, body_employer)
    assert new_employer['message'] == "Internal server error"


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
    new_employer_id = (employee.create_new_employee(token, new_employer))['id']
    
    info_employer = employee.get_info(new_employer_id)
    assert new_employer_id == info_employer['id']

def test_change_employer_info(get_token):
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
    just_employer = employee.create_new_employee(token, body_employer)
    id = just_employer['id']
    body_change = {
        "lastName": "Change",
        "email": "test@gmail.com",
        "url": "string",
        "phone": "string",
        "isActive": True
        }
    employer_change = employee.change_info(token, id, body_change)
    assert id == employer_change['id']
    assert body_employer["lastName"] != body_change["lastName"]

def test_get_list_employer(get_token):
    token = str(get_token)
    body_company = {
        "name": "NEW Company",
        "description": "string"
    }
    new_company = company.create_new_company(get_token, body_company)
    id_company= company.last_active_company()

    body_employer1 = {
            "id": 0,
            "firstName": "Employer1",
            "lastName": "Petrov",
            "middleName": "Nikolayevich",
            "companyId": id_company,
            "email": "testik@gmail.com",
            "url": 'string',
            "phone": "string",
            "birthdate": "2024-08-02T13:49:14.712Z",
            "isActive": True
        }
    employer1 = employee.create_new_employee(token, body_employer1)

    body_employer2 = {
            "id": 0,
            "firstName": "Employer2",
            "lastName": "IVANOV",
            "middleName": "Nikolayevich",
            "companyId": id_company,
            "email": "test@gmail.com",
            "url": 'string',
            "phone": "string",
            "birthdate": "2024-08-02T13:49:14.712Z",
            "isActive": True
        } 
    employer2 = employee.create_new_employee(token, body_employer2)

    list_employer = employee.get_list(id_company)
    assert len(list_employer) == 2
    








    


