from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=').text
soup=BeautifulSoup(html_text, 'lxml')
jobss=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for jobs in jobss:
    published_date=jobs.find('span',class_='sim-posted').span.text
    if 'few' in published_date:
        with open('posts/{jobs}.txt','w') as f:
            
            company_name=jobs.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=jobs.find('span', class_='srp-skills').text.replace(' ','')
            f.write(f'''
            Company Name:{company_name}
            Required Skills:{skills}
            ''')
            f.write('')