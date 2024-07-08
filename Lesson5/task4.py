from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

chrome.maximize_window()
firefox.maximize_window()
    
chrome.get("http://the-internet.herokuapp.com/entry_ad")
firefox.get("http://the-internet.herokuapp.com/entry_ad")

wait = WebDriverWait(chrome, 10)
Wait_firefox = WebDriverWait(firefox, 10)

Close_chrome = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
Close_chrome.click()

Close_firefox = Wait_firefox.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-footer")))
Close_firefox.click()

sleep(10)
