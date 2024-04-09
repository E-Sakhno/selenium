from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Иван")
    surname = browser.find_element(By.NAME, "lastname")
    surname.send_keys("Иванов")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("email")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)

    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)
    submit = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit.click()
    time.sleep(10)


finally:    
    browser.quit()

