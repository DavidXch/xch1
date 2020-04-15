from bs4 import BeautifulSoup
soup=BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)
print(soup.p)
print(type(soup.p))