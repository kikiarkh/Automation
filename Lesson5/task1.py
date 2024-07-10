from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.maximize_window()
firefox.maximize_window()

chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(5):
    chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()
    firefox.find_element(By.XPATH, '//button[text()="Add Element"]').click()

chrome_delete = chrome.find_elements(By.XPATH, '//button[text()="Delete"]')
firefox_delete = firefox.find_elements(By.XPATH, '//button[text()="Delete"]')

print(len(chrome_delete))
print(len(firefox_delete))

sleep(5)