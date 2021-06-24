from bs4 import BeautifulSoup
import requests

categories = [
'https://www.allrecipes.com/recipes/76/appetizers-and-snacks/',
'https://www.allrecipes.com/recipes/88/bbq-grilling/',
'https://www.allrecipes.com/recipes/156/bread/',
'https://www.allrecipes.com/recipes/78/breakfast-and-brunch/',
'https://www.allrecipes.com/recipes/79/desserts/',
'https://www.allrecipes.com/recipes/17562/dinner/',
'https://www.allrecipes.com/recipes/1642/everyday-cooking/',
'https://www.allrecipes.com/recipes/85/holidays-and-events/',
'https://www.allrecipes.com/recipes/17561/lunch/',
'https://www.allrecipes.com/recipes/80/main-dish/',
'https://www.allrecipes.com/recipes/92/meat-and-poultry/',
'https://www.allrecipes.com/recipes/95/pasta-and-noodles/',
'https://www.allrecipes.com/recipes/96/salad/',
'https://www.allrecipes.com/recipes/93/seafood/',
'https://www.allrecipes.com/recipes/81/side-dish/',
'https://www.allrecipes.com/recipes/94/soups-stews-and-chili/',
'https://www.allrecipes.com/recipes/236/us-recipes/',
'https://www.allrecipes.com/recipes/86/world-cuisine/'
]

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def readLinks():
    with open('link-lists/allrecipies.txt', 'r') as file:
        readLinks = file.readlines()
        return set([x.strip() for x in readLinks]) 

links = readLinks()

def addLinksToFile():
    with open('link-lists/allrecipies.txt', 'w') as file:
        for link in links:
            file.write(link + ' \n')

def showProgress(index, pageNumber):
    print(index, pageNumber, len(links))
    with open('link-lists/allrecipies_progress.txt', 'w') as file:
        file.write(f"{index} {pageNumber}")

def readProgress():    
    with open('link-lists/allrecipies_progress.txt', 'r') as file:
        progress_string = file.read()
        progress_list = progress_string.split()
        index = int(progress_list[0])
        pageNumber = int(progress_list[1])
        return [index, pageNumber]

def extractFirstPage(category_link):
    html_text = requests.get(category_link, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')

    outerDiv = soup.find_all('div', class_='card__imageContainer')
    for div in outerDiv: 
        link = div.find('a', class_='card__titleLink manual-link-behavior')['href']
        if link.find("/recipe/") != -1:
            links.add(link)
    outerDiv2 = soup.find_all('div', class_='category-page-item-content-wrapper')
    for div in outerDiv2:
        link = div.find('a', class_='category-page-item-image-text')['href']
        if link.find("/recipe/") != -1:
            links.add(link)

progress = readProgress()
startIndex = progress[0]
startPageNumber = progress[1]

for index, category_link in enumerate(categories):
    if (index < startIndex):
        continue

    pageNumber = startPageNumber

    if (pageNumber == 1):
        extractFirstPage(category_link)
        addLinksToFile()
        showProgress(index, pageNumber)
        pageNumber = 2

    response = requests.get('https://www.allrecipes.com/recipes/76/appetizers-and-snacks/' + '?page=' + str(pageNumber))
    while response.status_code == 200:
        html_text = response.text
        soup = BeautifulSoup(html_text, 'lxml')
        allLinks = soup.find_all('a', class_='tout__imageLink')
        for aTag in allLinks:
            link = 'https://www.allrecipes.com/' + aTag['href']
            links.add(link)
        addLinksToFile()
        showProgress(index, pageNumber)
        pageNumber = pageNumber + 1
        response = requests.get('https://www.allrecipes.com/recipes/76/appetizers-and-snacks/' + '?page=' + str(pageNumber))

print("Done")