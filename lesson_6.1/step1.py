from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.CSS_SELECTOR, "input[name=first-name]").send_keys("Иван")
last_name = driver.find_element(By.CSS_SELECTOR, "input[name=last-name]").send_keys("Петров")
address = driver.find_element(By.CSS_SELECTOR, "input[name=address]").send_keys("Ленина, 55-3")
email = driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]").send_keys("test@skypro.com")
phone = driver.find_element(By.CSS_SELECTOR, "input[name=phone]").send_keys("+7985899998787")
city = driver.find_element(By.CSS_SELECTOR, "input[name=city]").send_keys("Москва")
country = driver.find_element(By.CSS_SELECTOR, "input[name=country]").send_keys("Россия")
job_position = driver.find_element(By.CSS_SELECTOR,"input[name=job-position]").send_keys("QA")
company = driver.find_element(By.CSS_SELECTOR, "input[name=company]").send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

sleep(10)

#дальше ошибка. Не понимаю как проверить цвет???

zipcode = driver.find_element(By.CSS_SELECTOR, "#zip-code")
print(zipcode.value_of_css_property("background-color"))
assert zipcode == "rgba(248, 215, 218, 1)"

first_name_color = driver.find_element(By.CSS_SELECTOR, "#first-name")
print(first_name_color.value_of_css_property("background-color"))
assert first_name_color == "rgba(209, 231, 221, 1)"

last_name_color = driver.find_element(By.CSS_SELECTOR, "#last-name")
print(last_name_color.value_of_css_property("background-color"))
assert last_name_color == "rgba(209, 231, 221, 1)"

address_color = driver.find_element(By.CSS_SELECTOR, "#address")
print(address_color.value_of_css_property("background-color"))
assert address_color == "rgba(209, 231, 221, 1)"

email_color = driver.find_element(By.CSS_SELECTOR, "#e-mail")
print(email_color.value_of_css_property("background-color"))
assert email_color == "rgba(209, 231, 221, 1)"

phone_color = driver.find_element(By.CSS_SELECTOR, "#phone")
print(phone_color.value_of_css_property("background-color"))
assert phone_color == "rgba(209, 231, 221, 1)"

city_color = driver.find_element(By.CSS_SELECTOR, "#city")
print(city_color.value_of_css_property("background-color"))
assert city_color == "rgba(209, 231, 221, 1)"

country_color = driver.find_element(By.CSS_SELECTOR, "#country")
print(country_color.value_of_css_property("background-color"))
assert country_color == "rgba(209, 231, 221, 1)"

Job_position_color = driver.find_element(By.CSS_SELECTOR, "#job-position")
print(Job_position_color.value_of_css_property("background-color"))
assert Job_position_color == "rgba(209, 231, 221, 1)"

company_color = driver.find_element(By.CSS_SELECTOR, "#company")
print(company_color.value_of_css_property("background-color"))
assert company_color == "rgba(209, 231, 221, 1)"


sleep(50)
driver.quit()