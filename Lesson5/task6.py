from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.maximize_window()
firefox.maximize_window()

chrome.get("http://the-internet.herokuapp.com/login")
firefox.get("http://the-internet.herokuapp.com/login")

username = chrome.find_element(By.TAG_NAME, "input")
username.send_keys("tomsmith")

password = chrome.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

button = chrome.find_element(By.TAG_NAME, "button")
button.click()

username = firefox.find_element(By.TAG_NAME, "input")
username.send_keys("tomsmith")

password = firefox.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

button = firefox.find_element(By.TAG_NAME, "button")
button.click()


sleep(5)