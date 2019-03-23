import requests as req 
from bs4 import BeautifulSoup
import time
import re

#Key words to be matched for desired job openings
job_filter = ['javascript','spring','spring boot','pattern','web','framework']

#Save matching job details to a new file either by append or write
def save_file(data):
        f = open('job-detail.txt','a')
        f.write(job_title+'\n')
        f.write('----------------------------------------------------'+'\n')
        f.write(data.strip()+'\n')

#Save email address to new file
def email_address(data):
       
       email = re.findall(r'[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)',data)
       email_file = open('email.csv','a')
       email_file.write(str(email).strip())


#Passing url to fetch job detail
def job_detail(url):
    resp = req.get(url)
    job_detail_soup = BeautifulSoup(resp.text,'html.parser')
    job_detail= job_detail_soup.find('div',attrs={'class':'detail-text'})
    data = job_detail.text  
    match = False
    
    #Applying Filter to match keywords
    for f in job_filter:
        if(f.lower() in data):
            match = True
            break
    if(match):
            print('Successfully scraped!')
            email_address(data)
            save_file(data)
            
    else:
            print("Not Useful content")


# Search for URL to scrap the useful data and automate task

#Searching keywords to find the exact job search
content = req.post('https://www.jobsnepal.com/simple-job-search',data={'Keywords':'java'})

#HTML content parsing with Beautiful Soup
soup = BeautifulSoup(content.text,'html.parser')

#Selecting job-listing items 
jobs = soup.select('div.job-listing td a.job-item')

#Iterating within each job with their respective links
for job in jobs:
    job_title = job.text.strip()
    url = job.get('href')
    print('Scrapping for %s'%job_title)
    print('----------------------------------------------')
    #Function call for the details
    job_detail(url)
    print('-----------------------------------------------')
