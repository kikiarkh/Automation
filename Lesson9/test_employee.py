import pytest
import json
from Employee import Employer
from EmployerTable import EmployerTable

api = Employer("https://x-clients-be.onrender.com")
db = EmployerTable("postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

def test_create_new_employer():
    db.create_new_company("Cat and Dog", "description")
    max_id = db.get_max_id() 
    db_new_employer = db.create_new_employee(max_id, "Hello", "Kitty", "7777777777")
    new_employer_id = db.get_id_employer(max_id)
    api_employer_id = (api.get_info(new_employer_id))

    assert new_employer_id is not None
    assert api_employer_id["firstName"] == "Hello"
    
    db.delite_employer(new_employer_id)
    db.delite_company(max_id)

def test_get_info():

    name = "House"
    descr = "string"
    db.create_new_company(name, descr)
    max_id = db.get_max_id() 
    first_name = "Tom"
    last_name = "Kitty"
    phone = "79997778899"
    new_employer = db.create_new_employee(max_id, first_name, last_name, phone)
    new_id = db.get_id_employer(max_id)
    db_get_info = db.get_info(new_id)
    api_info_employer = api.get_info(new_id)

    assert api_info_employer["firstName"] == "Tom"
    assert api_info_employer["lastName"] == "Kitty"

    db.delite_employer(new_id)
    db.delite_company(max_id)

def test_change_employer_info():

    name = "House"
    descr = "string"
    db.create_new_company(name, descr)
    max_id = db.get_max_id() 
    first_name = "Tom"
    last_name = "Kitty"
    phone = "79997778899"
    new_employer = db.create_new_employee(max_id, first_name, last_name, phone)
    new_id = db.get_id_employer(max_id)
    new_name = "Jerry"
    db_change_info = db.change_info(new_name, new_id)
    api_change_info = api.get_info(new_id)

    assert api_change_info["firstName"] == "Jerry"

    db.delite_employer(new_id)
    db.delite_company(max_id)

def test_get_list_employer():

    name = "NEW Company"
    descr = "string"
    db.create_new_company(name, descr)
    max_id = db.get_max_id() 

    first_name = "Employer 1"
    last_name = "Petrov"
    phone = "79809876677"
    db.create_new_employee(max_id, first_name, last_name, phone)
    new_id_1 = db.get_id_employer(max_id)

    first_name = "Employer 2"
    last_name = "Ivanov"
    phone = "79999999999"
    db.create_new_employee(max_id, first_name, last_name, phone)
    new_id_2 = db.get_id_employer(max_id)

    db_list_employer = db.get_list(max_id).fetchall()
    api_list_employer = api.get_list(max_id)

    assert len(api_list_employer) == 2
    assert len(db_list_employer) == len(api_list_employer)
    assert api_list_employer

    db.delite_employer(new_id_1)
    db.delite_employer(new_id_2)
    db.delite_company(max_id)

    # pytest test_employee.py -v