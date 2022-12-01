import sqlite3
import json

class Hotel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

conn = sqlite3.connect('instance/banco.db')
cur = conn.cursor()

query = "Select * from hoteis"
resultado = cur.execute(query)

'''hotel = Hotel()
hotel['hotel_id'] = resultado['hotel_id']
hotel['nome'] = resultado['nome']
hotel['estrelas'] = resultado['estrelas']
hotel['diaria'] = resultado['diaria']
hotel['cidade'] = resultado['cidade']'''
colunas = ('hotel_id', 'nome', 'estrelas', 'diaria', 'cidade')
for registro in resultado:
    empacota_dic = dict(zip(colunas,registro))
    print(empacota_dic)
