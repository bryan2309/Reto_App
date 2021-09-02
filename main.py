import requests
from flask import Flask
from bs4 import BeautifulSoup
 
	#Autor: BRYAN SIMBAÑA
#entrega final de reto extraer información de yahoo finance y mostrarla a traves de una integración continua con Heroku	y Github Action	
	
app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
	return "El sitio web no se encuentra disponible, intente más tarde"

@app.route('/', methods=['GET'])
def index():

	headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
	crytoBitcoin='https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD'
	crytoEthereum ='https://finance.yahoo.com/quote/ETH-USD?p=ETH-USD'
	crytoCardano='https://finance.yahoo.com/quote/ADA-USD?p=ADA-USD'
	crytoBinanceCoin='https://finance.yahoo.com/quote/BNB-USD?p=BNB-USD'
	respuestaBitcoin=requests.get(crytoBitcoin,headers=headers)
	respuestaEthereum=requests.get(crytoEthereum,headers=headers)
	respuestaCardano=requests.get(crytoCardano,headers=headers)
	respuestaBinanceCoin=requests.get(crytoBinanceCoin,headers=headers)
	cadenaBitcoint=BeautifulSoup(respuestaBitcoin.text,'lxml')
	cadenaEthereum=BeautifulSoup(respuestaEthereum.text,'lxml')
	cadenaCardano=BeautifulSoup(respuestaCardano.text,'lxml')
	cadenabinancecoin=BeautifulSoup(respuestaBinanceCoin.text,'lxml')
	bitcoin=cadenaBitcoint.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	ethereum=cadenaEthereum.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	cardano=cadenaCardano.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	binancecoin=cadenaCardano.find('span',class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text.strip()
	return 'Valores de BITCOIN: $' + ' ' +bitcoin + ' ' + ' Valores de ETHEREUM $'+ ' ' +ethereum+ ' ' +' Valores de CARDANO $'+ ' ' +cardano+ ' ' +' Valores de BINANCE COIN $'+ ' ' +binancecoin+''
	

if __name__ == '__main__':
	app.run(port = PORT,debug = DEBUG)
