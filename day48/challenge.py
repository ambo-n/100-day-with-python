from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("tester1")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("tester1")
email = driver.find_element(By.NAME, value="email")
email.send_keys("tester1@mail.com")
button = driver.find_element(By.CSS_SELECTOR, value="button")
button.click()

driver.quit()