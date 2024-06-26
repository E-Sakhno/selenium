from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputName = browser.find_element(By.XPATH, '//label[text()="First name*"]//../input')
    inputName.send_keys("Ekaterina")
    inputSurname = browser.find_element(By.XPATH, '//label[text()="Last name*"]//../input')
    inputSurname.send_keys("Sakhno")
    inputEmail = browser.find_element(By.XPATH, '//label[text()="Email*"]//../input')
    inputEmail.send_keys("email@email.com")
    # inputPhone = browser.find_element(By.XPATH, '//label[text()="Phone:"]//../input')     
    # inputPhone.send_keys("+7999999999")
    # inputPhone = browser.find_element(By.XPATH, '//label[text()="Address:"]//../input')     
    # inputPhone.send_keys("Stavropol")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()