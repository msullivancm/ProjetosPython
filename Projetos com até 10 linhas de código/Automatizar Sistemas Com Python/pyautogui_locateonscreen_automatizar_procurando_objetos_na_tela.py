import pyautogui
import subprocess as sub
from time import sleep
#pip3 install opencv-python

def procura_e_clica(imagem, escreve, entra):
    #procura a barra de busca do browser
    pyautogui.locateCenterOnScreen(imagem, confidence=0.8)
    if escreve:
        pyautogui.write(escreve)
    if entra:
        pyautogui.hotkey('enter')

#procura dentro do site, escreve e entra
#buscar = pyautogui.prompt(text='', title='O que gostaria de buscar?')
buscar = 'quem é o maior ladrão'

#link a ser aberto
link='youtube.com'
#abre o browser
#sub.Popen(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",shell=True)
#ou se quiser só usar o pyautogui pra tudo, também é possível
pyautogui.hotkey("win","r") #pressiona a tecla windows ou super mais letra r
pyautogui.write("msedge.exe")
pyautogui.hotkey("enter")
#aguarda abertura
sleep(3)
#procura barra de busca, escreve e entra
procura_e_clica('imagens/barra_busca_edge.png', link, True)
sleep(5)
#procurar no youtube o que foi escrito no popup
procura_e_clica('imagens/barra_busca_youtube.png', buscar, True)
sleep(5)



