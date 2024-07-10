from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.maximize_window()
firefox.maximize_window()

chrome.get("http://the-internet.herokuapp.com/inputs")
firefox.get("http://the-internet.herokuapp.com/inputs")

number = chrome.find_element(By.TAG_NAME, "input")
number.send_keys("1000")
sleep(2)
number.clear()
sleep(2)
number.send_keys("999")

number = firefox.find_element(By.TAG_NAME, "input")
number.send_keys("1000")
sleep(2)
number.clear()
number.send_keys("999")

sleep(5)