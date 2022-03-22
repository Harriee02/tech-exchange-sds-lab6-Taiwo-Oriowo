#Teammate: Evolone Layne
from flask import Flask
from flask import render_template
from flask import request
from model import checkAnswer


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results',methods = ["GET", "POST"])
def results():
    point = 0
    if request.method == "GET":
        return render_template("index.html")
    else:
        answer = {"New York": request.form["New York"], "California": request.form["California"],"Alabama": request.form["Alabama"] , "Ohio": request.form["Ohio"] , "Utah": request.form["Utah"]}
        results = checkAnswer(answer)
        newYork = results["New York"]
        california = results["California"]
        alabama = results["Alabama"]
        ohio = results["Ohio"]
        utah = results["Utah"]
        if newYork:
            point += 1
        if california:
            point += 1
        if alabama:
            point += 1
        if ohio:
            point += 1
        if utah:
            point += 1
        return render_template('scorepage.html', point= point, newYork=newYork, california = california, alabama=alabama, ohio=ohio, utah=utah)
        