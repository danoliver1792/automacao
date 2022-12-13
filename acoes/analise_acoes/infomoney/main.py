from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# verificando a versão do navegador e baixando o drive relacionado
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# entrando no site
driver.get('https://www.infomoney.com.br/')
sleep(2)

# coletando tabela de maiores altas das ações no dia
dados1 = driver.find_element(By.ID, 'high').text
print(dados1)
