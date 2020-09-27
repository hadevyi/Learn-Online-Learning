from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")  # project name
db = {}                       # fake DB


@app.route("/")  # someone taping /
def home():
    #return "Hello! Welcome to mi sasa!"
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get('word')

    if word:
        word = word.lower()  # formatting
        existingJobs = db.get(word)
        
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)


@app.route("/export")
def export() :
  try :
    word = request.args.get('word')

    if not word :
      raise Exception()    
    
    word = word.lower()  # formatting
    jobs = db.get(word)

    if not jobs :
      raise Exception()
    
    save_to_file(jobs)
    return send_file("jobs.csv", as_attachment=True)
  except :
        return redirect("/")
'''
# dynamic URL
@app.route("/<username>") # not equal route and function name, @ is see just-under flask
def contact(username) :
  return F"Hello {username} how are you doing"
'''

app.run(host="0.0.0.0")
