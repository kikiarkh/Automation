from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.maximize_window()
firefox.maximize_window()
    
chrome.get("http://uitestingplayground.com/classattr")
firefox.get("http://uitestingplayground.com/classattr")

chrome.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
chrome.switch_to.alert.accept()
firefox.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
firefox.switch_to.alert.accept()

for x in range(3):
    chrome.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    chrome.switch_to.alert.accept()
    firefox.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    firefox.switch_to.alert.accept()

sleep(5)