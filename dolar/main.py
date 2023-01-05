from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pyautogui as pg

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get('https://www.google.com.br/')
sleep(3)

browser.maximize_window()
sleep(3)
browser.find_element(By.NAME, 'q').send_keys('dolar hoje')
sleep(4)
browser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
sleep(4)

valueDollar = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
print(valueDollar)
