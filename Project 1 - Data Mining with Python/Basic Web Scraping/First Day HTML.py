from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.gunnerkrigg.com/archives/")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h4)