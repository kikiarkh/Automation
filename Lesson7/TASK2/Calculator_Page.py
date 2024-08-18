from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def insert_time(self):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(45)

    def value1(self):
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()

    def sum(self):
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()

    def value2(self):
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()

    def equal(self):
        self.driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def result(self):
        WebDriverWait(self.driver, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        
    

