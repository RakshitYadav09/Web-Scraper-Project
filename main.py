from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
soup=BeautifulSoup(html_text, 'lxml')
jobs=soup.find('li', class_='clearfix job-bx wht-shd-bx')
company_name=jobs.find('h3',class_='joblist-comp-name').text.replace(' ','')
skills=jobs.find('span', class_='srp-skills').text.replace(' ','')
print(skills)
print(company_name)