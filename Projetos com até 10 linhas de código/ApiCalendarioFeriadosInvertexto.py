'''import requests 
import time
from tqdm import tqdm
from datetime import datetime, timedelta
from workadays import workdays as wd
import datetime as dt

#link = 'https://api.invertexto.com/v1/holidays/2022?token=2072|XP6Aaaz4nhBX90CT3GeEnzHxs0WBMW9J'
link = 'https://api.invertexto.com/v1/holidays/2022?token=2072|XP6Aaaz4nhBX90CT3GeEnzHxs0WBMW9J&state=rj'

def entre_datas(dataini, datafin):
    um_dia = timedelta(days = 1)
    atual = dataini
    while atual < datafin:
        yield atual
        atual += um_dia
        
def extrai_feriados():
    req = requests.get(link)
    return req

def convert_data_timestamp(data):
    time_stamp = time.mktime(datetime.strptime(data, '%d/%m/%Y').timetuple())
    return time_stamp 



def converte_data_padrao(data):
    if '-' in data: 
        data_lista = data.split('-')    
    elif '/' in data: 
        data_lista = data.split('/')
    data_convertida = f'{data_lista[-1]},{data_lista[-2]},{data_lista[-0]}'
    return data_convertida

def feriados_no_periodo(dataini, datafin):
    dataini = converte_data(dataini)
    datafin = converte_data(datafin)
    feriados = extrai_feriados()
    conta_feriados_no_periodo = 0
    for f in feriados.json():
        #print(f"Data inicio {dataini}, data final {datafin}, feriado {f['date']}")
        if f['date'] >= dataini and f['date'] <= datafin:
            conta_feriados_no_periodo += 1
    return conta_feriados_no_periodo

def dias_semana(dataini, datafin):
    dataini = converte_data_padrao(dataini)
    datafin = converte_data_padrao(datafin)
    conta_dias_semana = 0
    for d in entre_datas(dataini, datafin):
        if d.weekday() not in (5, 6):
            print (d, d.weekday())
            conta_dias_semana += 1
    return conta
            
def dias_uteis(dataini, datafin):
    qtd_dias_uteis = wd.networkdays(dt.date(converte_data_padrao(dataini)), dt.date(converte_data_padrao(datafin)))
    qtd_feriados = feriados_no_periodo(dataini, datafin)
    dataini = convert_data_timestamp(dataini)
    datafin = convert_data_timestamp(datafin)
    req = extrai_feriados()
    qtd_dias_uteis_com_feriados = qtd_dias_uteis.days - qtd_feriados
    return qtd_feriados, qtd_dias_uteis.days, qtd_dias_uteis_com_feriados
    
print(dias_uteis('01/12/2022','31/12/2022')) #retorna quantidade de feriados, dias uteis e dias uteis já incluindo os feriados
'''
from workadays import workdays as wd
import datetime as dt
import requests

def converte_data(data,separador,tupla):
    if '-' in data: 
        data_lista = data.split('-')    
    elif '/' in data: 
        data_lista = data.split('/')
    if tupla:
        ano = data_lista[-1]
        mes = data_lista[-2]
        dia = data_lista[0]
        dt_data = dt.date(int(ano), int(mes), int(dia))
        return dt_data
    else: 
        data_convertida = f'{data_lista[-1]}{separador}{data_lista[-2]}{separador}{data_lista[0]}'
        return data_convertida

def qtd_feriados_entre_datas(dataini, datafin):
    dataini = converte_data(dataini,'-', False)
    datafin = converte_data(datafin,'-', False)
    link = 'https://api.invertexto.com/v1/holidays/2022?token=2072|XP6Aaaz4nhBX90CT3GeEnzHxs0WBMW9J&state=rj'
    req = requests.get(link)
    qtd = 0
    for d in req.json():
        if d['date']>=dataini and d['date']<=datafin:
            qtd +=1
    return qtd

def qtd_dias_uteis(dataini, datafin):
    dataini = converte_data(dataini, ',',True)
    datafin = converte_data(datafin, ',',True)
    qtd = wd.networkdays(dataini, datafin, country='BR', state='RJ')
    return qtd
    
print(f"Quantidade de feriados no período {qtd_feriados_entre_datas('01/12/2022', '31/12/2022')}")
print(f"Quantidade de dias útes {qtd_dias_uteis('01/12/2022','31/12/2022')}")
print(f"Quantidade de dias útes contando com os feriados {qtd_dias_uteis('01/12/2022','31/12/2022') - qtd_feriados_entre_datas('01/12/2022', '31/12/2022')}")
