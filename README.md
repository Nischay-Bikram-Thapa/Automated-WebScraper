# Automated-WebScraper

## Author: Nischay Thapa

### Looking for the job description manually and comparing with your skills might be time-consuming. So why not automate?
------------------------------------------------------------------------------------------------------------------------------
This is a repository for scraping data from a job portal and selecting relevant job titles and description which is equivalent to your qualification.

Description
-----------------
Mentioned below is the algorithm on how the process works

1. Initally scraping of data from the url using requests library.
2. Using BeautifulSoup to parse html content.
3. Searching the relevant job-title and extract the content from the nested url
4. Applying filters with keywords to match the job description. For instance, your resume might contain certain keywords which would be        useful to search jobs which are convenient.
5. If the filters match to the description, extract the email address and the job description from the source to respond with attachments.
