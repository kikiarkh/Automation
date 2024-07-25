from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pytest 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from Mine_Page import MinePage

browser = webdriver.Chrome()
Mine_Page = MinePage(browser)

def test_first_name():
    Mine_Page.first_name("Иван")

def test_last_name():
    Mine_Page.last_name("Петров")

def test_address():
    Mine_Page.address("Ленина, 55-3")

def test_email():
    Mine_Page.email("test@skypro.com")

def test_phone():
    Mine_Page.phone("+7985899998787")

def test_city():
    Mine_Page.city("Москва")

def test_country():
    Mine_Page.country("Россия")

def test_job_position():
    Mine_Page.job_position("QA")

def test_company():
    Mine_Page.company("SkyPro")

def test_sunmit():
    Mine_Page.submit()

def test_color_zip():
    Mine_Page.color_zip()

def test_color_firstname():
    Mine_Page.color_firstname()

def test_color_lastname():
    Mine_Page.color_lastname()

def test_color_address():
    Mine_Page.color_address()

def test_color_email():
    Mine_Page.color_email()

def test_color_city():
    Mine_Page.color_city()

def test_color_country():
    Mine_Page.color_country()

def test_color_job_position():
    Mine_Page.color_job_position()

def test_color_company():
    Mine_Page.color_company()

driver.implicitly_wait(10)

driver.quit()

#pytest page_object_task1.py