'''# instalar https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/
#no instalador do visual studio, selecionar o componente MSVC 14 e instalar
from bs4 import BeautifulSoup as bs 
from lxml import etree
import requests

html = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').content 
#strong , .secondaryInfo , .titleColumn a -> pega lista de filmes com ano e avaliação
#//*[contains(concat( " ", @class, " " ), concat( " ", "titleColumn", " " ))]

soup = bs(html, 'html.parser')
dom = etree.HTML(str(soup))

print(dom.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "titleColumn", " " ))]'))
'''

from bs4 import BeautifulSoup
from lxml import etree
import requests


URL = "https://en.wikipedia.org/wiki/Nike,_Inc."

HEADERS = ({'User-Agent':
			'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
			(KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
			'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))
print(dom.xpath('//*[@id="firstHeading"]')[0].text)
