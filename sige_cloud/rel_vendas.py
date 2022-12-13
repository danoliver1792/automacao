from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pyautogui as pya

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.sigecloud.com.br/')

# maximizando tela
navegador.maximize_window()
sleep(2)

# entrando no sistema
navegador.find_element(By.XPATH, '//*[@id="nav"]/li[6]/a').click()
sleep(3)
navegador.find_element(By.XPATH, '//*[@id="txtEmail"]').send_keys('adm3@agilesteel.com.br')
sleep(3)
navegador.find_element(By.XPATH, '//*[@id="txtPass"]').send_keys('123456789')
sleep(3)
navegador.find_element(By.XPATH, '//*[@id="btnEntrar"]').click()
sleep(8)

# baixando relatorio de vendas
pya.click(x=349, y=143)
sleep(3)
pya.click(x=417, y=411)
sleep(8)
pya.click(x=1037, y=504)
sleep(3)
pya.click(x=1047, y=570)
sleep(5)
pya.click(x=1040, y=622)
sleep(2)
pya.click(x=1033, y=573)
sleep(2)
pya.click(x=165, y=567)
sleep(2)
pya.click(x=504, y=332)
sleep(6)
pya.click(x=504, y=332)
sleep(6)
pya.click(x=1122, y=256)
sleep(5)
pya.click(x=1160, y=345)
sleep(8)

# fechando o navegador
navegador.close()
print('Download da planilha de vendas concluido')
