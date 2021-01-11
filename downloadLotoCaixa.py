#!/usr/bin/python
import requests, zipfile, os

arquivos = ['D_megase.zip', 'D_lotfac.zip']
link = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/'
BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + '\\files\\jogos_sorteados'

def download_descompactar():
	#BASE_PATH = os.path.dirname(os.path.abspath(__file__))
	print('Caminho Base: ' + BASE_PATH)

	for arquivo in arquivos:
		print('Arquivo: ' + arquivo)
		request = requests.get(link + arquivo)
		file = 'files/jogos_sorteados/' + arquivo
		with open(file, 'wb') as code:
			code.write(request.content)
		print('Download Concluído.')
		zip = zipfile.ZipFile(BASE_PATH + '/' + arquivo)
		zip.extractall(BASE_PATH)
		zip.close()
		print('Extração Concluída.\n')

	#request = requests.get('http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip')
	#with open('D_lotfac.zip', 'wb') as code:
	#	code.write(request.content)
	
	
def write_zip():
	#BASE_PATH = os.path.dirname(os.path.abspath(__file__))
	zip = zipfile.ZipFile(BASE_PATH + '/D_lotfac.zip')
	zip.write(BASE_PATH, compress_type=zipfile.ZIP_DEFLATED)
	

if __name__ == '__main__':
	download_descompactar();
