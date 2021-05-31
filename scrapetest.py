from urllib.request import urlopen
#from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://ja.wikipedia.org/wiki/Category:%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').findAll('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries though!')
    for link in bs.findAll('a', href = re.compile('^(/wiki/)')):
            if 'href' in link.attrs:
                if link.attrs['href'] not in pages:
                    newPage = link.attrs['href']
                    print('----------------\n'+newPage)
                    pages.add(newPage)
                    getLinks(newPage)

getLinks('')
# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen('http://ja.wikipedia.org/wiki/Category:%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     for link in bs.findAll('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 #새 페이지를 발견
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)

#getLinks('')

# 카테고리 내 페이지 키워드 크롤링
# html = urlopen('https://ja.wikipedia.org/wiki/Category:%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%82%BF')
# bs = BeautifulSoup(html, 'html.parser')
# for link in bs.find('div', {'id':'mw-pages'}).findAll('a',
#                     href = re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


# for child in bs.find('div', {'id': 'mw-pages'}).li.children:
#     print(child)

# 정규 표현식으로 위치를 정확하게 산출 할 수 없을 때 찾는 방법
# images = bs.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for image in images:
#     print(image['src'])


# for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
#     print(sibling)

# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bs = BeautifulSoup(html.read(), 'html.parser')
#         title = bs.body.h1
#     except AttributeError as e:
#         return None
#     return title
#
# title = getTitle('http://www.pythonscraping.com/pages/warandpeace.html')
# if title == None:
#     print('Title could not be found')
# else:
#     print(title)