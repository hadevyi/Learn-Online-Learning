from flask import Flask

app = Flask("SuperScrapper") # project name

@app.route("/") # someone taping /
def home() :
  return "Hello! Welcome to mi sasa!"

@app.route("/contact") # not equal route and function name, @ is see just-under flask
def contact() :
  return "Contant me!"

app.run(host="0.0.0.0")