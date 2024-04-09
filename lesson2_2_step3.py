from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    num1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    print(num1, num2)
    res = num1+num2
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
    time.sleep(10)


finally:    
    browser.quit()

