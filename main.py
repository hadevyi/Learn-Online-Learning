from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()           # calculration max page
indeed_jobs = extract_indeed_jobs(last_indeed_page) # each page scrapping
print(indeed_jobs)                                  # result print dict(title, company, location, apply url)
