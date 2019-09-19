# Imports
import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

__author__ = "Connor Nelson"

"""
This program was our introduction to forms. It goes to both google and coinmarketcap in order
to compare prices and display the cheapest prices for Bitcoin and Bitcoin Cash. Then it prints 
out all of the prices as well as identifies the cheapest one and prints it out. 
"""

def get_price_coinmarket(searchTerm): 
	"""
	This method retrieves the price of a cryptocurrency by going to coinmarket and searching for the 
	input term in their form. Then it goes to the first link on the page of results.
	From their it finds the price on the page for that cryptocurrency. Then it returns that price. 
	"""
	coinmarketresponse = requests.get("https://coinmarketcap.com/search/", params = {"q" :searchTerm})
	bsObj = BeautifulSoup(coinmarketresponse.text, "html.parser")
	page = bsObj.find("ul", {"class" : "search-results"}).find("a")["href"]
	url = "https://coinmarketcap.com/" + page +"/"
	webpage = urlopen(url)
	fullPage = BeautifulSoup(webpage, "html.parser")
	price = float((fullPage.find("span", {"class" : "h2 text-semi-bold details-panel-item--price__value"})).text)
	return price

def get_page_link_coinmarket(searchTerm):
	"""
	Was the original method when it came down to gettting the links from coinmarket in order to 
	find the price. Has been incorperted into get_price_coinmarket. 
	"""
	#coinmarketresponse = requests.get("https://coinmarketcap.com/search/?q=Bitcoin", params = {"q" :"searchTerm"})
	coinmarketresponse = requests.get("https://coinmarketcap.com/search/?q=" + searchTerm, params = {"q" :searchTerm})
	bsObj = BeautifulSoup(coinmarketresponse.text, "html.parser")
	pageLink = bsObj.find("ul", {"class" : "search-results"}).find("a")["href"]
	print(pageLink)
	return(pageLink)

def get_google_price(searchTerm):
	"""
	This method finds the price of a cryptocurrency by making a request from google using 
	the inputted search term. It sees what google has listed as the price and then parses and 
	takes out the price of the currency. This method is operational for any currency that google
	takes data on. 
	"""
	findPrice = re.compile(r"[0-9]+\.[0-9]+")
	googleResponse = requests.get("https://www.google.at/search?", params = {"q" : searchTerm})
	bsObj = BeautifulSoup(googleResponse.text, "html.parser")
	price = bsObj.find("div", {"class" : "J7UKTe"}).text
	price = price.replace(",","")
	priceFinal = findPrice.findall(price)[0]
	priceFinal = float(priceFinal)
	return priceFinal

def get_form_data(link):
	"""
	Simple method using Ceasar's code in order to find the needed input for forms.
	prints them out row by row in format "name : value"
	"""
	homeresponse = requests.get(link)
	bsObj = BeautifulSoup(homeresponse.text, "html.parser")
	input_tags = bsObj.form.find("input")
	print(input_tags)
	for tag in input_tags:
		print(tag['name'] + " : " + tag.get('value',''))

def floatToString(inputValue):
	"""
	Takes in gloat and removes 0s
	"""
	return ('%.2f' % inputValue).rstrip('0').rstrip('.')

def print_prices():
	"""
	Utilizes the above methods in order to print the price for Bitcoin and Bitcoin Cash
	from both Coinmarketcap and Google. Then it prints out the cheapest price out of them 
	labeled with the site that it came from. 
	"""
	BTCCMC = floatToString(get_price_coinmarket("Bitcoin"))
	BTCGoogle = floatToString(get_google_price("Price of Bitcoin"))
	BCHCMC = floatToString(get_price_coinmarket("Bitcoin Cash"))
	BCHGoogle = floatToString(get_google_price("Price of Bitcoin Cash"))
	if BTCCMC > BTCGoogle:
		BTC = ("Google", BTCGoogle)
	else:
		BTC = ("Coinmarketcap", BTCCMC)
	if BCHCMC > BCHGoogle:
		BCH = ("Google", BCHGoogle)
	else:
		BCH = ("Coinmarketcap", BCHCMC)
	print("Bitcoin Price CMC: $" + BTCCMC)
	print("Bitcoin Price Google: $" + BTCGoogle)
	print("Bitcoin Cash Price CMC: $" + BCHCMC)
	print("Bitcoin Cash Price Google: $" + BCHGoogle)
	print("CHEAPEST PRICES")
	print("Bitcoin:", BTC[0], "with a price of $" + BTC[1])
	print("Bitcoin Cash:", BCH[0], "with a price of $" + BCH[1])
if __name__ == '__main__':
	print_prices()