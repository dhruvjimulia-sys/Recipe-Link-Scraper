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

links = set()

for category_link in range(1):
    html_text = requests.get('https://www.allrecipes.com/recipes/76/appetizers-and-snacks/').text
    soup = BeautifulSoup(html_text, 'lxml')
    outerDiv = soup.find_all('div', class_='card__imageContainer')
    for div in outerDiv: 
        link = div.find('a', class_='card__titleLink manual-link-behavior')['href']
        if link.find("/recipe/") != -1:
            print(link)
            links.add(link)

    outerDiv2 = soup.find_all('div', class_='category-page-item-content-wrapper')
    for div in outerDiv2:
        link = div.find('a', class_='category-page-item-image-text')['href']
        if link.find("/recipe/") != -1:
            print(link)
            links.add(link)

    pageNumber = 2
    response = requests.get('https://www.allrecipes.com/recipes/76/appetizers-and-snacks/' + '?page=' + str(pageNumber))
    while response.status_code == 200:
        print(pageNumber)
        html_text = response.text
        soup = BeautifulSoup(html_text, 'lxml')
        allLinks = soup.find_all('a', class_='tout__imageLink')
        for aTag in allLinks:
            link = aTag['href']
            links.add(link)
            print(link)
        pageNumber = pageNumber + 1
        response = requests.get('https://www.allrecipes.com/recipes/76/appetizers-and-snacks/' + '?page=' + str(pageNumber))

print(links)
print(len(links))

def extractFirstPage(soup):
    outerDiv = soup.find_all('div', class_='card__imageContainer')
    for div in outerDiv: 
        link = div.find('a', class_='card__titleLink manual-link-behavior')['href']
        if link.find("/recipe/") != -1:
            print(link)
            links.add(link)

    outerDiv2 = soup.find_all('div', class_='category-page-item-content-wrapper')
    for div in outerDiv2:
        link = div.find('a', class_='category-page-item-image-text')['href']
        if link.find("/recipe/") != -1:
            print(link)
            links.add(link)