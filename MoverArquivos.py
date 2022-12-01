#Objetivo
# Mover arquivos e subdiretórios da esquerda para direita
from tqdm import tqdm
import shutil
import os

De_Para = [
    (r'D:\Roms\RAGBOXV2_32GB\3-Jogos\ps1\225 Jogos PS1 - Completos',r'D:\Roms\RAGBOXV2_32GB\3-Jogos\ps1'),
    (r'D:\Roms\Jogos de PS1',r'D:\Roms\RAGBOXV2_32GB\3-Jogos\ps1')
    ]

def move_esq2dir(source, destination):
    files = os.listdir(source) #carrega lista de arquivos dentro do diretório source
    if os.path.isdir(source) and os.path.isdir(destination):
        for file in files:
            try:
                if os.path.isfile(f'{source}/{file}'):
                    if os.path.isdir(destination):
                        new_path = shutil.move(f"{source}/{file}", destination)
                    else: 
                        os.makedirs(destination)
                        new_path = shutil.move(f"{source}/{file}", destination)
            except:
                pass

for i in tqdm(De_Para):
    move_esq2dir(i[0], i[1])