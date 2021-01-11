#!/usr/bin/python
from bs4 import BeautifulSoup

import downloadLotoCaixa
import os.path

arquivo = None
soup = None

path = 'files/jogos_sorteados/d_lotfac.htm'

def findValueTD(row):
	return [td.get_text() for td in row.find_all("td")]

def findNumber(numberList):
	return [int(numberList[indice]) for indice in range(2, 17)]

def printValues(dados):
	[print(valor) for valor in dados]

# The first tr contains the field names.
#headings = [th.get_text().strip() for th in table.find("tr").find_all("th")]
def createListNumber():
	arquivo = open(path, 'r', encoding='iso-8859-1')
	soup = BeautifulSoup(arquivo.read(), "html.parser")
	table = soup.find("table")
	datasets = []
	for row in table.find_all("tr"):
		dataset = findValueTD(row)
		if len(dataset) > 18:
			dataset = findNumber(dataset)
			dataset.sort()
			datasets.append(dataset)

	arquivo.close()
	#print(datasets)
	return datasets

if __name__ == '__main__':
	if not os.path.isfile(path):
		downloadLotoCaixa.download_descompactar()
	printValues(createListNumber())
