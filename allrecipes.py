from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.allrecipes.com/recipes/').text
soup = BeautifulSoup(html_text, 'lxml')

recipe_category_links = soup.find_all('li', class_='carouselNav__listItem recipeCarousel__listItem')
print(recipe_category_links)


with open('')