from turtle import width
import pyautogui as pg 
import webbrowser as web
import time 
import pandas as pd

data_dict = data.to_dict('list')
data = pd.read_excel(r"C:\Users\User\Documents\python\automacao\whatsapp\contatos.xlsx")
leads = data_dict['whatsapp']
messages = data_dict['msg']
combo = zip(leads,messages)
nome = True
for lead,message in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    if nome:
        time.sleep(6)
        nome = False
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(8)
    pg.press('esc')
    time.sleep(5)
    pg.press('enter')
    time.sleep(10)
    pg.hotkey('ctrl', 'w')
print('Mensagens enviadas com sucesso')
