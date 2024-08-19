from sqlalchemy import create_engine, text


class EmployerTable:

    __scripts =  {
        "select": text("select * from company"),
        "max_id": text("select MAX(id) from company"),
        "insert_company": text("insert into company(name, description) values (:company_name, :description)"),
        "insert_employer": text("insert into employee(company_id, first_name, last_name, phone) values (:id, :name, :surname, :phone)"),
        "list_employer": text("select * from employee where company_id = :select_id"),
        "delite_by_id": text("delete from company where id = :id_to_delete"),
        "id_employer": text("select MAX(id) from employee where company_id = :c_id"),
        "update_employer": text("update employee set first_name = :new_name where id = :employer_id"),
        "delite_employer": text("delete from employee where id = :id_delete")
        }

    def __init__(self, engine):
        self.db = create_engine(engine)

    def get_max_id(self):
        with self.db.connect() as connection:
            result = connection.execute(self.__scripts["max_id"]).fetchall()[0][0]
        return result

    def create_new_company(self, name: str, description: str):
        with self.db.connect() as connection:
            result = connection.execute(self.__scripts["insert_company"], parameters=dict(company_name=name, description = description))
            connection.commit()
        return result

    def create_new_employee(self, company_id, first_name, last_name, phone):
        with self.db.connect() as connection:
            result = connection.execute(self.__scripts["insert_employer"], parameters=dict(id = company_id, name = first_name, surname = last_name, phone = phone))
            connection.commit()
        return result

    def get_list(self, company_id):
        with self.db.connect() as connection:
            result = connection.execute(self.__scripts["list_employer"], parameters=dict(select_id = company_id))
        return result

    def delite_company(self, id):
        with self.db.connect() as connection:
            connection.execute(self.__scripts["delite_by_id"], parameters=dict(id_to_delete = id))
            connection.commit()

    def get_id_employer(self, company_id):
        with self.db.connect() as connection:
            result = connection.execute(self.__scripts["id_employer"], parameters=dict(c_id=company_id)).fetchall()[0][0]
        return result

    def get_info(self, id):
        with self.db.connect() as connection:
            result=  connection.execute(self.__scripts["list_employer"], parameters=dict(select_id = id))
            connection.commit()
        return result

    def change_info(self, new_name, id):
        with self.db.connect() as connection:
            result = connection.execute(self.__scripts["update_employer"], parameters=dict(new_name = new_name, employer_id = id))
            connection.commit()
        return result
    
    def delite_employer(self, id):
        with self.db.connect() as connection:
            connection.execute(self.__scripts["delite_employer"],parameters=dict(id_delete = id))
            connection.commit()

           



