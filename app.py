from flask import Flask, render_template, request, flash, redirect
from random import randint
import json, random, beers
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        result = request.form['abv']
        button = request.form['b']
        if button==None:
            return render_template("home.html")
        else:            
            #check the input
            if len(result)>3:
                flash("Invalid ABV number, must be an INT or a DOUBLE.")
                return redirect("/")
            try:
                abv = float(result)
            except:
                flash("Invalid ABV number, must be an INT or a DOUBLE.")
                return redirect("/")
            return page(abv)

@app.route("/result", methods=["GET", "POST"])
def page(abv):
    #get a random pony image
    id = randint(0,100)
    url1 = "http://ponyfac.es/api.json/id:" + str(id)
    request1 = urllib2.urlopen(url1)
    resultstring1 = request1.read()
    d1 = json.loads(resultstring1)
    try:
        link = d1["faces"][0]["thumbnail"]
    except:
        link = "http://ponyfac.es/1/thumb"

    output = [abv, beers.get_beers(abv), 
              link.encode('ascii', 'ignore')]
    return render_template("page.html", result = output)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4321)
