#importa modulos necessários
#Baixar o webdriver do firefox em https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-win32.zip
#descompactar o executável no caminho de instalação dos binários do python
#conda install selenium
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(options=options, executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe")

#informa endereço do smartclient web e autenticação
link = f"https://s02ashm03.ferroport.com.br:8156/"
usuario = 'admin'
senha = 'P@ssw0rd2126#'
programaInicial = 'sigacfg'
ambiente = 'FRP_P12133_TESTE'

driver.get(link)
time.sleep(2) 

elemento=driver.find_element_by_xpath("//input[@id='inputStartProg']")
elemento.click()
elemento.clear()
elemento.send_keys(programaInicial)
elemento=driver.find_element_by_xpath("//input[@id='inputEnv']")
elemento.click()
elemento.clear()
elemento.send_keys(ambiente)
elemento.send_keys(Keys.TAB)
elemento=driver.find_element_by_xpath("//button[@class='button button-ok']").click()
