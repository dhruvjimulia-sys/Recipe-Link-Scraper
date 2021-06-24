from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def readLinks():
    with open('link-lists/foodcom.txt', 'r') as file:
        readLinks = file.readlines()
        return set([x.strip() for x in readLinks]) 

links = readLinks()

def addLinksToFile():
    with open('link-lists/foodcom.txt', 'w') as file:
        for link in links:
            file.write(link + ' \n')

def showProgress(index, pageNumber_):
    print(index, pageNumber_, len(links))
    with open('link-lists/foodcom_progress.txt', 'w') as file:
        file.write(f"{index} {pageNumber_}")

