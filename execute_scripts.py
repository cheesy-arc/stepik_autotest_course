from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(10)
finally:
    browser.quit()
