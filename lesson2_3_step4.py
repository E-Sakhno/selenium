from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element(By.ID, "input_value").text
    input = browser.find_element(By.ID, "answer")
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    submit = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit.click()
    time.sleep(10)


finally:    
    browser.quit()

