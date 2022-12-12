from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# instalando o ChromeDriver e entrando no site
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://economia.uol.com.br/cotacoes/bolsas/') 

# pesquisando a acao desejada - Petrobras
inputBusca = driver.find_element(By.ID, 'filled-normal')
inputBusca.send_keys('PETR3.SA')
sleep(2)
inputBusca.send_keys(Keys.ENTER)
sleep(3)

# capturando o valor da acao
spanValue = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
cotacaoValue = spanValue.text
print(f'Valor da cotacao da PETR3.SA: {cotacaoValue}')

input('')
