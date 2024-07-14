from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

driver.find_element(By.CSS_SELECTOR, "#checkout").click()

driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ekaterina")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Rybakova")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("1234567")

driver.find_element(By.CSS_SELECTOR, "#continue").click()

driver.implicitly_wait(10)

total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text
assert total == "Total: $58.29"

print(total)

driver.quit()