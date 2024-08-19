from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pytest 
import allure

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from Mine_Page import MinePage

browser = webdriver.Chrome()
Mine_Page = MinePage(browser)

@allure.title("Проверка написания имени")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_first_name():
    Mine_Page.first_name("Иван")

@allure.title("Проверка написания фамилии")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_last_name():
    Mine_Page.last_name("Петров")

@allure.title("Проверка написания адреса")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_address():
    Mine_Page.address("Ленина, 55-3")

@allure.title("Проверка написания email")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_email():
    Mine_Page.email("test@skypro.com")

@allure.title("Проверка написания телефона")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_phone():
    Mine_Page.phone("+7985899998787")

@allure.title("Проверка написания города")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_city():
    Mine_Page.city("Москва")

@allure.title("Проверка написания страны")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_country():
    Mine_Page.country("Россия")

@allure.title("Проверка написания рабочей специальности")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_job_position():
    Mine_Page.job_position("QA")

@allure.title("Проверка написания компании")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_company():
    Mine_Page.company("SkyPro")

@allure.title("Нажатие на кнопку Submit")
@allure.feature("CREATE")
@allure.severity("BLOCKER")
def test_sunmit():
    Mine_Page.submit()

@allure.title("Проверка цвета поля color-zip")
@allure.description("Проверить, что цвет поля rgba(248, 215, 218, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_zip():
    Mine_Page.color_zip()

@allure.title("Проверка цвета поля first-name")
@allure.description("Проверить, что цвет поля rgba(209, 231, 221, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_firstname():
    Mine_Page.color_firstname()

@allure.title("Проверка цвета поля last-name")
@allure.description("Проверить, что цвет поля rgba(209, 231, 221, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_lastname():
    Mine_Page.color_lastname()

@allure.title("Проверка цвета поля address")
@allure.description("Проверить, что цвет поля rgba(209, 231, 221, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_address():
    Mine_Page.color_address()

@allure.title("Проверка цвета поля email")
@allure.description("Проверить, что цвет поля rgba(209, 231, 221, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_email():
    Mine_Page.color_email()

@allure.title("Проверка цвета поля city")
@allure.description("Проверить, что цвет поля rgba(209, 231, 221, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_city():
    Mine_Page.color_city()

@allure.title("Проверка цвета поля country")
@allure.description("Проверить, что цвет поля rgba(209, 231, 221, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_country():
    Mine_Page.color_country()

@allure.title("Проверка цвета поля job-position")
@allure.description("Проверить, что цвет поля rgba(209, 231, 221, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_job_position():
    Mine_Page.color_job_position()

@allure.title("Проверка цвета поля company")
@allure.description("Проверить, что цвет поля rgba(209, 231, 221, 1)")
@allure.feature("READ")
@allure.severity("BLOCKER")
def test_color_company():
    Mine_Page.color_company()

driver.implicitly_wait(10)

driver.quit()

#pytest page_object_task1.py