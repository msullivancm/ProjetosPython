import pyautogui
from time import sleep
import subprocess as sub

# Passos manuais
# Abrir o programa
sub.Popen('app.exe',shell=True)
# 1 - Clicar e digitar o usuário
pyautogui.click(945,539,duration=1)
pyautogui.write('jhonatan')
# 2 - Clicar e digitar a senha
pyautogui.click(945,571)
pyautogui.write('123456')
# 3 - Clicar em Entrar
pyautogui.click(844,606)
# 4 - Ler cada linha da lista de produtos
listaProdutos = []
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        
        pyautogui.click(598,526) 
        pyautogui.write(produto) 
        pyautogui.click(598,559)
        pyautogui.write(quantidade)
        pyautogui.click(595,589)
        pyautogui.write(preco)
        pyautogui.click(495,787,duration=1) 
        sleep(1)
# 	1 - Clicar e digitar produtos
# 	2 - clicar e digitar quantidade
# 	3 - clicar em registrar
# Coordenadas
# 945,539 login
# 945,571 senha
# 844,606 entrar
# 598,526 Produto
# 598,559 Quantidade
# 595,589 Preço
# 495,787 Registrar
