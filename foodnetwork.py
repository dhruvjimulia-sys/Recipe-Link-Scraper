from bs4 import BeautifulSoup
import requests
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

def readLinks():
    with open('link-lists/foodnetwork.txt', 'r') as file:
        readLinks = file.readlines()
        return set([x.strip() for x in readLinks]) 

links = readLinks()

def addLinksToFile():
    with open('link-lists/foodnetwork.txt', 'w') as file:
        for link in links:
            file.write(link + ' \n')

def showProgress(index, pageNumber_):
    print(index, pageNumber_, len(links))
    with open('link-lists/foodnetwork_progress.txt', 'w') as file:
        file.write(f"{index} {pageNumber_}")

def readProgress():    
    with open('link-lists/foodnetwork_progress.txt', 'r') as file:
        progress_string = file.read()
        progress_list = progress_string.split()
        index = int(progress_list[0])
        pageNumber_ = int(progress_list[1])
        return [index, pageNumber_]

progress = readProgress()
startIndex = progress[0]
startPageNumber = progress[1]
pageNumber = startPageNumber

categories = []

def generateCategoryLinks():
    for i in range(97, 120):
        categories.append('https://www.foodnetwork.com/recipes/recipes-a-z/' + chr(i))
    categories.append('https://www.foodnetwork.com/recipes/recipes-a-z/xyz')

generateCategoryLinks()

for index, category_link in enumerate(categories):
    if (index < startIndex):
        continue

    response = requests.get(category_link  + '/p/' + str(pageNumber))
    while response.status_code == 200:
        html_text = response.text
        soup = BeautifulSoup(html_text, 'lxml')
        all_list_elements = soup.find_all('li', class_='m-PromoList__a-ListItem')
        for list_element in all_list_elements:
            link = 'https:' + list_element.find('a')['href']
            links.add(link)
        addLinksToFile()
        showProgress(index, pageNumber)
        pageNumber = pageNumber + 1
        response = requests.get(category_link  + '/p/' + str(pageNumber))
    pageNumber = 1

print("Done")