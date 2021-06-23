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

print(categories)


# html_text = requests.get('https://www.allrecipes.com/recipes/').text
# soup = BeautifulSoup(html_text, 'lxml')