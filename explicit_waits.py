from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = 'https://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))
    book = browser.find_element(By.CSS_SELECTOR, '#book')
    book.click()
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)
    submit = browser.find_element(By.CSS_SELECTOR, '#solve')
    submit.click()
    time.sleep(10)
finally:
    browser.quit()
