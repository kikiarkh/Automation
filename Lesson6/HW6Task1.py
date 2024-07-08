from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()

driver.implicitly_wait(40)
green_text = driver.find_element(By.CSS_SELECTOR,".bg-success").text

print(green_text)