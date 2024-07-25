from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def authorization(self):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def products(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def shopping_cart(self):
        self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()

    def checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    def my_data(self):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ekaterina")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Rybakova")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("1234567")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def total(self):
       total_price = self.driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text
       total = "Total: $58.29"
       return total_price


    



    