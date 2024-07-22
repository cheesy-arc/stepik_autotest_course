from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys('Валерий')
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys('Жмышенко')
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys('петрович@яндексточкару')
    attach_button = browser.find_element(By.CSS_SELECTOR, '#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    attach_button.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(10)
finally:
    browser.quit()
