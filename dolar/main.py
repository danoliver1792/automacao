from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pyautogui as pg
import xlsxwriter as xw
import os

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
browser.get('https://www.google.com.br/')
sleep(3)

# pesquisando o valor do Dolar
browser.maximize_window()
sleep(3)
browser.find_element(By.NAME, 'q').send_keys('dolar hoje')
sleep(4)
browser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
sleep(4)

# capturando o valor do Dolar
valueDollar = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
print(valueDollar)

# limpando o campo de pesquisa e buscando pelo valor do Euro
sleep(4)
browser.find_element(By.NAME, 'q').send_keys('')
sleep(4)
pg.press('tab')
sleep(4)
pg.press('enter')
sleep(4)
browser.find_element(By.NAME, 'q').send_keys('Euro hoje')
sleep(4)
browser.find_element(By.NAME, 'q').send_keys(Keys.RETURN)
sleep(4)

# capturando o valor do Euro
valueEuro = browser.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
print(valueEuro)
sleep(3)

# escrevendo os valores coletados em uma planilha do Excel
filePath = r'C:\Users\User\Documents\python\automacao\dolar_euro.xlsx'
excelCreated = xw.Workbook(filePath)
excel1 = excelCreated.add_worksheet()

excel1.write('A1', 'Dolar')
excel1.write('B1', 'Euro')
excel1.write('A2', valueDollar)
excel1.write('B2', valueEuro)

valueDollar = valueDollar.replace(',', '.')
valueEuro = valueEuro.replace(',', '.')

valueDollarTipoFloat = float(valueDollar)
valueEuroTipoFloat = float(valueEuro)

excel1.write('A3', valueDollarTipoFloat)
excel1.write('B3', valueEuroTipoFloat)


excelCreated.close()

# fechando e abrindo o arquivo
excelCreated.close()
os.startfile(filePath)
