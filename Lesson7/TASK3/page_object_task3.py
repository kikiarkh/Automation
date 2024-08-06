from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from shop_page import Shop

browser = webdriver.Chrome()
shop_page = Shop(browser)

def test_authorization():
    shop_page.authorization()

def test_products():
    shop_page.products()

def test_shopping_cart():
    shop_page.shopping_cart()


def test_checkout():
    shop_page.checkout()


def test_my_data():
    shop_page.my_data()

total = "Total: $58.29"

def test_total():
    shop_page.total()
    assert total in shop_page.total()
    print(shop_page.total)
   
driver.quit()

#pytest page_object_task3.py