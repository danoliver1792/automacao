from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

# instalando o Chrome Driver Manager
servico = Service(ChromeDriverManager().install())
# usando o servico instalado
navegador = webdriver.Chrome(service=servico)

# entrando em um website
navegador.get("https://login.live.com/")

# preenchimento dos campos
navegador.find_element('xpath', '//*[@id="i0116"]').send_keys('danrlei.jesus@hotmail.com')
sleep(2)
navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
sleep(3)
navegador.find_element('xpath', '//*[@id="i0118"]').send_keys('*******')
sleep(2)
navegador.find_element('xpath', '//*[@id="idSIButton9"]').click()
