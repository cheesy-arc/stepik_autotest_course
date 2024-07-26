from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'https://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    price = browser.find_element(By.CSS_SELECTOR, '#price')
    price.text
    book = browser.find_element(By.CSS_SELECTOR, '#book')
    book.clik()
finally:
    browser.quit()
