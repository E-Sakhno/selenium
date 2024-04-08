from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    x_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(str(math.log(abs(12*math.sin(int(x_value))))))
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobutton.click()
    submit = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    submit.click()
    time.sleep(10)


finally:    
    browser.quit()

