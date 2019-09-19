#Imports
import re
import queue
import requests
from queue import PriorityQueue
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Array of all stopwords 
stopwords = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']

""" Project Primus
    Uses a sereies of methods to create a bot that travereses wikipedia to 
    go from one web page to another. The implementing method is wikiladder and 
    it utilizes a list of stopwords as well as it does not check duplicates. 
    There is a method to utilize a priority queue and also a basic one that 
    uses a simple queue.
"""
__author__ = "Connor Nelson"
def wikiladder(startPage, endPage):
    """ This function returns a list of the wikipedia links (as page titles) 
        that one could follow to get from the startPage to the endPage. 
        The returned list includes both the start and end pages. If either page is 
        invalid it returns a empty list
    """
    if not check_webpage(startPage) or not check_webpage(endPage):
        return []
    path = find_path_priority(startPage, endPage)
    #print(path)
    for i in range(len(path)):
        path[i] = hrefToString(path[i])
    path = path + [endPage]
    return path


def hrefToString(s):
    """ 
    Turns webpage with /wiki/ into just the page name 
    """
    return s[6:]

def find_path(startPage, endPage):
    """
    Takes in a start page and an endpage and returns a tuple wth the path at the
    first postion and the end page in the secone position. This is the basic method 
    using a simple queue which is unsorted and is just first in last out.
    """
    testedSet = {""} #Set of all tested links
    pathArray = []
    startingTuple = (pathArray, "/wiki/" + startPage)
    pagesQueue = queue.Queue() #Creates the queue that is used to parse
    pagesQueue.put(startingTuple)
    while not pagesQueue.empty():
        activeTuple = pagesQueue.get()
        if activeTuple[1] not in testedSet and hrefToString(activeTuple[1]) not in stopwords:
            print(activeTuple[1]) #prints the tuple that is is currently working on
            testedSet.add(activeTuple[1])
            linksList = get_links_list(activeTuple[1])
            if "/wiki/" + endPage in linksList: #Checks to see if the pages that is being worked contains the end page
                return activeTuple[0] +[activeTuple[1]]
            else:
                newPath = activeTuple[0] + [activeTuple[1]]
                for j in linksList: #Adds all of the links from the 
                    addTuple = (newPath, j)
                    pagesQueue.put(addTuple)

def find_path_priority(startPage, endPage):
    """
    Takes in a start page and an endpage and returns a tuple wth the path at the
    first postion and the end page in the secone position. It is the same as the 
    original method but it uses a priorty queue instead. It uses the default 
    sorting algorithim which just sorts the queue alphabetically. 
    """
    testedSet = {"", "a"} #Set of all tested links
    pathArray = []
    startingTuple = (pathArray, "/wiki/" + startPage)
    pagesQueue = queue.PriorityQueue()
    pagesQueue.put(startingTuple)
    while not pagesQueue.empty():
        activeTuple = pagesQueue.get()
        if activeTuple[1] not in testedSet and activeTuple[1] not in stopwords:
            print(activeTuple[1])
            testedSet.add(activeTuple[1])
            linksList = get_links_list(activeTuple[1])
            if "/wiki/" + endPage in linksList:
                return activeTuple[0] +[activeTuple[1]]
            else:
                newPath = activeTuple[0] + [activeTuple[1]]
                for j in linksList: #Adds all of the links to the queue with the path to get to them in the first spot in the tuple
                    addTuple = (newPath, j)
                    pagesQueue.put(addTuple)

def get_links_list(page_name):
    """ 
    Creates a list of all the useable links based on the page name on wikipedia that is given.
    Then it returns that list. 
    """
    url = "https://en.wikipedia.org/" + page_name
    html = urlopen(url)
    webpage = BeautifulSoup(html, "html.parser")
    link_list = webpage.find("div", {"id":"bodyContent"}).findAll("a",{"href":re.compile("^\/wiki\/[^:]*$")}) #Gets all of the links that are usable
    for i in range(len(link_list)): #Gets rid of the tag and gives it the href not the text displayed
        link_list[i] = link_list[i]['href']
    return link_list

def check_webpage(page_name):
    """
    Checks to see if a webpage extists on wikipedia based on the page link. 
    """
    url = "https://en.wikipedia.org/wiki/" + page_name
    resp = requests.head(url)
    if resp.status_code == 200: #Webpage exists
        return True
    else: 
        return False

if __name__ == '__main__':
    # put your test code here
    # print(get_links_list("Lion"))
    print(wikiladder("Emu", "Duke_University"))
