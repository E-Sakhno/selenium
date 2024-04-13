from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book = browser.find_element(By.ID, "book")
    book.click()
    x = browser.find_element(By.ID, "input_value").text
    input = browser.find_element(By.CSS_SELECTOR, "#answer")
    input.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    submit = browser.find_element(By.ID, "solve")
    submit.click()
    answer = browser.switch_to.alert
    print(answer.text)
    time.sleep(30)



finally:    
    browser.quit()

