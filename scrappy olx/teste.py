from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def uf(esc):
    if esc == 1:
        esco = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[6]/div/div/div/div[2]/div/div[1]/div[1]/div/a").click() # DDD 11 - São Paulo e região
    else:
        print('Falha')

    return esco


def ar(esc):

    if esc == 1:
        escol = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[6]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/a").click() # Centro
    else:
        print('Falha')
        
    return escol


tipo = input('Qual objeto: ')
estado = input('Qual estado: ')
area = input('Qual area: ')

driver = webdriver.Chrome()
driver.get("https://www.olx.com.br")
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/input").send_keys(tipo, Keys.ENTER)
driver.implicitly_wait(0.5)
uf(estado)
driver.implicitly_wait(0.5)
ar(area)
