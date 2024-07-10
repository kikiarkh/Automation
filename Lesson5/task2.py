from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.maximize_window()
firefox.maximize_window()
    
chrome.get("http://uitestingplayground.com/dynamicid")
firefox.get("http://uitestingplayground.com/dynamicid")


chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
firefox.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

for x in range(3):
    button_chrome = chrome.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    button_chrome = firefox.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()

sleep(5)