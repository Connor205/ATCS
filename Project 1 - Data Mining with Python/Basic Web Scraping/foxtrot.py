from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
import re

__author__ = "Connor Nelson"
#Opening and Reading in HTML
html = urlopen("https://www.ptable.com")
bsObj = BeautifulSoup(html, "html.parser")

#Getting List of atomic masses - goodlist is final list
linkedList = bsObj.findAll('i')
goodlist = []
for i in range(len(linkedList)):
	goodlist.append(linkedList[i].getText())
	goodlist[i] = goodlist[i].replace('(',"").replace(')',"")
goodlist.remove("Weight")
for i in range(len(goodlist)):
	goodlist[i] = float(goodlist[i])

#FGetting list of the lanthonoid Elements 
lanthanoidElementsList = bsObj.findAll("td", {"class":"Element Lanthanoid f"})
lanthanoidElementsList2 = bsObj.findAll("td", {"class":"Element Lanthanoid d"})
lanthanoidElementsListM = []
for item in lanthanoidElementsList:
	lanthanoidElementsListM.append(float(item.i.getText().replace('(',"").replace(')',"")))
lanthanoidElementsList2 = float(lanthanoidElementsList2[0].i.getText().replace('(',"").replace(')',"")) #Dealing with 1 wacky case
average = (sum(lanthanoidElementsListM) + lanthanoidElementsList2)/(len(lanthanoidElementsListM) +1) #Taking the average of the lanthonoids masses

#Creating list of atomic numbers 
atomicNumberListM = []
matcher = re.compile("\d+")
atomicNumberList = bsObj.findAll("strong", {"an":matcher})
for i in range(len(atomicNumberList)):
	atomicNumberList[i] = float(atomicNumberList[i].getText())

#Identifying the element in the lists with most nuetrons(highest difference)
num_most_neutrons = 0
index_most_neutrons = []
for i in range(len(atomicNumberList)):
	if goodlist[i] - atomicNumberList[i] > num_most_neutrons:
		num_most_neutrons = goodlist[i] - atomicNumberList[i]
		index_most_neutrons = []
		index_most_neutrons.append(i)
	if goodlist[i] - atomicNumberList[i] == num_most_neutrons and not i in index_most_neutrons:
		index_most_neutrons.append(i)

#Creating List of Elements to parse
elememts_list = []
elememts_list = bsObj.findAll("em")
for i in range(len(elememts_list)):
	elememts_list[i] = elememts_list[i].getText()
elememts_list.remove("Name")

elem_most_neutrons = []
for i in index_most_neutrons:
	elem_most_neutrons.append(elememts_list[i])

#Printing Results
print("The sum of one mole of all of the elements on the periodic table is: %fg" % (sum(goodlist)))
print("The mean mass of the the lanthanoid elements is: %fg" % average)
print("The elements with the most nuetrons are", elem_most_neutrons)