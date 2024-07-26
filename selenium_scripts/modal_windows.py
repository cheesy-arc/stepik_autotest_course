from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'https://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, '.form-control')
    input.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(10)

finally:
    browser.quit()
