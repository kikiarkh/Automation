from sqlalchemy import create_engine 
from sqlalchemy.sql import text 


class EmployerTable:

    __scripts =  {
        "select": "select * from company",
        "max_id": "select MAX(id) from company",
        "insert_company": text("insert into company(\"name\", \"description\") values (:new_name, :descr)"),
        "insert_employer": text("insert into employee(company_id, first_name, last_name, phone) values (:id, :name, :surname, :phone)"),
        "list_employer": text("select * from employee where company_id = :select_id"),
        "delite_by_id": text("delete from company where id = :id_to_delete"),
        "id_employer": "select MAX(id) from employee",
        "update_employer": text("update employee set first_name = :new_name where id = :employer_id")
        }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_max_id(self):
        self.db.execute(self.__scripts["max_id"]).fetchall()[0][0]


    def create_new_company(self, name: str, description: str):
        self.db.execute(self.__scripts["insert_company"], new_name = name, descr = description).fetchall()

    def create_new_employee(self, company_id, first_name, last_name, phone):
        self.db.execute(self.__scripts["insert_employer"], id = company_id, name = first_name, surname = last_name, phone = phone).fetchall()

    def get_list(self, company_id):
        self.db.execute(self.__scripts["list_employer"], select_id = company_id).fetchall()

    def delite_company(self, id):
        self.db.execute(self.__scripts["delite_by_id"], id_to_delete = id).fetchall()

    def get_id_employer(self):
        self.db.execute(self.__scripts["id_employer"]).fetchall()[0][0]

    def get_info(self, id):
        self.db.execute(self.__scripts["list_employer"], select_id = id).fetchall()

    def change_info(self, new_name, id):
        self.db.execute(self.__scripts["update_employer"],new_name = new_name, employer_id = id).fetchall()


