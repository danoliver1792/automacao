from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# entrando no site dos Correios
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www2.correios.com.br/sistemas/precosprazos/')
sleep(2)
driver.maximize_window()
sleep(3)

# Informando o CEP de origem e destino
driver.find_element(By.NAME, 'cepOrigem').send_keys('81610170')
sleep(1)
driver.find_element(By.NAME, 'cepDestino').send_keys('44645000')
sleep(2)

# Selecionando o tipo PAC
Select(driver.find_element(By.NAME, 'servico')).select_by_index(15)
sleep(2)

# Selecionando o tipo da embalagem
Select(driver.find_element(By.NAME, 'embalagem1')).select_by_index(2)

# Informando as dimensões da embalagem e valor da mercadoria
driver.find_element(By.NAME, 'Altura').send_keys('10')
sleep(1)
driver.find_element(By.NAME, 'Largura').send_keys('10')
sleep(1)
driver.find_element(By.NAME, 'Comprimento').send_keys('15')
sleep(1)
driver.find_element(By.NAME, 'peso').send_keys('3')
sleep(1)
driver.find_element(By.NAME, 'ckValorDeclarado').click()
sleep(2)
driver.find_element(By.NAME, 'valorDeclarado').send_keys('3000')
sleep(1)
driver.find_element(By.NAME, 'Calcular').click()
sleep(2)

# entrando na aba e pegando as informacoes - tempo de entrega e preco
driver.switch_to.window(driver.window_handles[1])
tempoEntrega = driver.find_elements(By.CLASS_NAME, 'destaque')[0].find_element(By.TAG_NAME, 'td').text
print(tempoEntrega)

preco = driver.find_elements(By.CLASS_NAME, 'destaque')[1].find_element(By.TAG_NAME, 'td').text
print(preco)

driver.close()
