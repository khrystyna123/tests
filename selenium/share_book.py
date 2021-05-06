#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import geckodriver_autoinstaller

geckodriver_autoinstaller.install()

driver = webdriver.Firefox()
driver.get("http://localhost:8000/login")

wait = WebDriverWait(driver, 10)

email = driver.find_element_by_name("email")
password = driver.find_element_by_name("password")
login = driver.find_element_by_class_name("loginbtn")

email.send_keys("user@gmail.com")
password.send_keys("password")

login.click()

assert driver.find_element_by_class_name("name").text == "user"


wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "browse"))).click()

assert driver.find_element_by_class_name("signupbtn").text == "Search"


wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="http://localhost:8000/books/1"]'))).click()

assert driver.find_element_by_class_name("b_title").text == "Officia consequuntur possimus vitae."


wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "share"))).click()

assert driver.find_element_by_class_name("login_word").text == "SHARE BOOK"


condition = driver.find_element_by_id("condition")
share = driver.find_element_by_class_name("loginbtn")

condition.send_keys("good")

share.click()

assert driver.find_element_by_class_name("b_title").text == "Officia consequuntur possimus vitae." and driver.find_element_by_id("user").text == "SHARED BY: user" and driver.find_element_by_id("condition").text == "CONDITION: good"

driver.quit()