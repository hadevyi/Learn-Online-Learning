import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = F"https://www.indeed.com/jobs?q=python&limit={LIMIT}" # the web is USA, not Korea

def extract_indeed_pages() :
  result = requests.get(URL)
  #print(indeed_result.text)                                # You can see HTRML code

  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class" : "pagination"})
  links = pagination.find_all('a')

  pages = []
  for link in links[0:-1] :
    pages.append(int(link.string))                          # is equlas "link.find("span").string"
  max_page = pages[-1]                                      # is equlas max(pages)

  return max_page

def extract_job(html) :
  title = html.find("h2", {"class" : "title"}).find("a")["title"]
  company = html.find("span", {"class" : "company"}) 
  company_anchor = company.find("a")

  if company_anchor is not None :                           # Bez, Sometime location is empty.
    company = str(company_anchor.string)
  else :
    company = str(company.string)

  company = company.strip()

  #location = html.find("span", {"class" : "location"}).string          
  location = html.find("div", {"class" : "recJobLoc"})["data-rc-loc"]
  #print(location)

  job_id = html["data-jk"]

  return {"title" : title, 
  "company" : company, 
  "location" : location,
  "link" : F"https://www.indeed.com/viewjob?jk={job_id}"}


def extract_indeed_jobs(last_page) :
  jobs = []
  for page in range(last_page) :
    print(F"Scrappting page {page}")
    result = requests.get(F"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
    for result in results :
      job = extract_job(result)
      jobs.append(job)
  return jobs