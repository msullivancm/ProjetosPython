#importa modulos necessários
#Baixar o webdriver do firefox em https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-win32.zip
#descompactar o executável no caminho de instalação dos binários do python
#conda install selenium
import selenium
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

driver = webdriver.Chrome()

#options = Options()
#options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
#driver = webdriver.Firefox(options=options, executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe")

#informa endereço do smartclient web e autenticação
link = f"https://s02ashm03.ferroport.com.br:8156/"
usuario = 'admin'
senha = 'P@ssw0rd2126#'
programaInicial = 'sigacfg'
ambiente = 'FRP_P12133_TESTE'
usuarioOrigem = 'filipe.santana'
usuarioDestino = 'acesso'
senhaDestino = 'acesso00'

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
time.sleep(6)
elemento=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[4]/div[3]/input")
elemento.click()
elemento.clear()
elemento.send_keys(usuario)
time.sleep(2)
elemento.send_keys(Keys.TAB)
elemento=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[4]/div[5]/input")
elemento.click()
elemento.clear()
elemento.send_keys(senha)
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[4]/div[9]/button").click()


time.sleep(5)
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[5]/div[15]/button").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/ul/li[5]/label").click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="COMP3112"]/label').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="COMP3116"]/label').click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/div[1]/button").click()
time.sleep(2)
elemento=driver.find_element_by_xpath('//*[@id="COMP6020"]/input')
time.sleep(2)
elemento.click()
elemento.clear()
elemento.send_keys(usuarioOrigem)
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div[2]/div[3]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[5]/div/table/tbody/tr[1]/td[3]/div").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div[3]/div/div[3]/button").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/ul/li[6]/label").click()
time.sleep(2)
elemento=driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/input")
time.sleep(2)
elemento.send_keys(usuarioDestino)
time.sleep(2)
elemento=driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[4]/input")
time.sleep(2)
elemento.send_keys(senhaDestino)
time.sleep(2)
elemento=driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[5]/input")
time.sleep(2)
elemento.send_keys(senhaDestino)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/div[3]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div[1]/button").click()
time.sleep(2)
driver.close()