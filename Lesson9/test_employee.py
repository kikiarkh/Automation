import pytest
from Employee import Employer
from EmployerTable import EmployerTable

api = Employer("https://x-clients-be.onrender.com")
db = EmployerTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def test_create_new_employer():

    new_name = "Cats and Dogs"
    descr = "описание"
    db.create_new_company(new_name, descr)
    max_id = db.get_max_id() 

    company_id = max_id
    first_name = "Hello"
    last_name = "Kitty"
    phone = "77777777777"
    db_new_employer = db.create_new_employee(company_id, first_name, last_name, phone)

    new_employer_id = db_new_employer['id']
    api_new_employer = api.get_list(company_id)[0]

    assert new_employer_id is not None
    assert db_new_employer == api_new_employer
    

    db.delite_company(company_id)

def test_get_info():

    name = "House"
    descr = "string"
    db.create_new_company(name, descr)
    max_id = db.get_max_id() 

    company_id = max_id
    first_name = "Tom"
    last_name = "Kitty"
    phone = "79997778899"
    new_employer = db.create_new_employee(company_id, first_name, last_name, phone)

    new_id = db.get_id_employer()

    db_get_info = db.get_info(new_id)
    api_info_employer = api.get_info(new_id)

    assert new_id == db_get_info['id']
    assert api_info_employer == db_get_info

    db.delite_company(company_id)

def test_change_employer_info():

    name = "House"
    descr = "string"
    db.create_new_company(name, descr)
    max_id = db.get_max_id() 

    company_id = max_id
    first_name = "Tom"
    last_name = "Kitty"
    phone = "79997778899"
    new_employer = db.create_new_employee(company_id, first_name, last_name, phone)

    new_id = db.get_id_employer()
    new_name = "Jerry"

    db_change_info = db.change_info(new_name, new_id)
    api_change_info = api.get_info(new_id)

    assert db_change_info == api_change_info

    db.delite_company(company_id)

def test_get_list_employer():

    name = "NEW Company"
    descr = "string"
    db.create_new_company(name, descr)
    max_id = db.get_max_id() 

    company_id = max_id
    first_name = "Employer 1"
    last_name = "Petrov"
    phone = "79809876677"
    db.create_new_employee(company_id, first_name, last_name, phone)

    first_name = "Employer 2"
    last_name = "Ivanov"
    phone = "79999999999"
    db.create_new_employee(company_id, first_name, last_name, phone)

    db_list_employer = db.get_list(company_id)

    api_list_employer = api.get_list(company_id)
    assert len(db_list_employer) == 2
    assert db_list_employer == api_list_employer

    db.delite_company(company_id)

    #pytest test_employee.py -v