from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x = browser.find_element(By.ID, "input_value").text
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    submit2 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    submit2.click()
    answer = browser.switch_to.alert
    print(answer.text)
    time.sleep(10)



finally:    
    browser.quit()

