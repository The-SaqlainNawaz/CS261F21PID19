from selenium import webdriver
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome(executable_path='C:\\Users\Hassan Nawaz\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe')
basic = 'https://yts.mx/browse-movies/0/all/all/0/featured/0/all'
nextt = '?page=0'
array = []
for i in range(1, 2):
    add = basic + nextt + str(i)
    driver.get(add)
    content = driver.page_source
    soup = BeautifulSoup(content)
    # print (soup)
    for a in soup.findAll('div', attrs={'class': 'browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4'}):
        name = a.find('div', attrs={'class': 'browse-movie-bottom'}).find('a', attrs={'href': re.compile("^https://")})
        # print(name.get('href'))
        driver.get(name.get('href'))
        content = driver.page_source
        soup = BeautifulSoup(content)
        for b in soup.findAll('div', attrs={'class': 'col-xs-10 col-sm-14 col-md-7 col-lg-8 col-lg-offset-1'}):
            title = b.find('div', attrs={'class': 'hidden-xs'}).find('h1').text
            year = b.find('div', attrs={'class': 'hidden-xs'}).findAll('h2')
            rating = b.find('div', attrs={'class': 'bottom-info'}).find('div',
                                                                        attrs={'itemprop': 'aggregateRating'}).find(
                'span', attrs={'itemprop': 'ratingValue'}).text

            print()
            print(title)
            print()
            print(year[0].text)
            print(year[1].text)
            print(rating)
            print()
        for c in soup.findAll('div', attrs={'class': 'col-sm-10 col-md-7 col-lg-offset-1'}):
            try:
                director = c.find('div', attrs={'class': 'directors'}).find('div', attrs={'class': 'list-cast'}).find(
                    'div', attrs={'class': 'list-cast-info tableCell'}).find('a', attrs={'class': 'name-cast'}).find(
                    'span', attrs={'itemprop': 'director'}).find('span', attrs={'itemprop': 'name'}).text
                print(director)
            except:
                director = "unknown"
                print(director)
            try:
                actors = c.find('div', attrs={'class': 'actors'}).findAll('div', attrs={'class': 'list-cast'})
                for i in range(len(actors)):
                    ac1 = []
                    ac1.append(actors[i].find('div', attrs={'class': 'list-cast-info tableCell'}).find('span', attrs={
                        'itemprop': 'name'}).text)
                    print(ac1)
            except:
                print("cast is unknown")
        for e in soup.findAll('div', attrs={'id': 'movie-sub-info'}):
            try:
                synop = e.find('div', attrs={'id': 'synopsis'}).find('p', attrs={'class': 'hidden-xs'}).text
                print(synop)
            except:
                print("no synop")