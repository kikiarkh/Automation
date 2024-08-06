from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from Calculator_Page import Calculator

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

browser = webdriver.Chrome()
Calculator_Page = Calculator(browser)

def test_insert_time():
    Calculator_Page.insert_time()

def test_value1():
    Calculator_Page.value1()

def test_sum():
    Calculator_Page.sum()

def test_value2():
    Calculator_Page.value2()

def test_equal():
    Calculator_Page.equal()

def test_result():
    Calculator_Page.result

driver.quit()

#pytest page_object_task2.py