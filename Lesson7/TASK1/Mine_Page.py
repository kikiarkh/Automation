from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class MinePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def first_name(self, term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=first-name]").send_keys(term)

    def last_name(self, term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=last-name]").send_keys(term)

    def address(self, term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=address]").send_keys(term)

    def email(self, term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]").send_keys(term)

    def phone(self, term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=phone]").send_keys(term)

    def city(self, term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=city]").send_keys(term)

    def country(self, term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=country]").send_keys(term)

    def job_position(self, term):
        self.driver.find_element(By.CSS_SELECTOR,"input[name=job-position]").send_keys(term)

    def company(self, term):
        self.driver.find_element(By.CSS_SELECTOR, "input[name=company]").send_keys(term)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        self.driver.implicitly_wait(5)

    def color_zip(self):
        color_zip = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        assert color_zip == "rgba(248, 215, 218, 1)"

    def color_firstname(self):
        color_firstname = self.driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
        assert color_firstname == "rgba(209, 231, 221, 1)"

    def color_lastname(self):
        color_lastname = self.driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color")
        assert color_lastname == "rgba(209, 231, 221, 1)"

    def color_address(self):
        color_address = self.driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color")
        assert color_address == "rgba(209, 231, 221, 1)"

    def color_email(self):
        color_email = self.driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color")
        assert color_email == "rgba(209, 231, 221, 1)"

    def phone_color(self):
        color_phone = self.driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color")
        assert color_phone == "rgba(209, 231, 221, 1)"

    def color_city(self):
        color_city = self.driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color")
        assert color_city == "rgba(209, 231, 221, 1)"

    def color_country(self):
        color_country = self.driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color")
        assert color_country == "rgba(209, 231, 221, 1)"

    def color_job_position(self):
        color_job_position = self.driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color")
        assert color_job_position == "rgba(209, 231, 221, 1)"

    def color_company(self):
        color_company = self.driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")
        assert color_company == "rgba(209, 231, 221, 1)"

    



    

    





