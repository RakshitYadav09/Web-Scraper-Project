from bs4 import BeautifulSoup

with open ('Allinone _ Web Scraper Test Sites.html', 'r') as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content, 'lxml')
    tags=soup.find_all('h4')
    print(tags)