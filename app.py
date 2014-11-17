from flask import Flask, render_template, request, flash, redirect
from random import randint
import json, random, beers
try:
    import urllib.request as urllib2
    import urllib.parse as urllib
except ImportError:
    import urllib2
    import urllib

app = Flask(__name__)
app.secret_key = "w0w-beer-and-pony"

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
    try:
        output = [abv, beers.get_beers(abv), 
                  link.encode('ascii', 'ignore')]
    except:
        flash("Invalid ABV number, must be an INT or a DOUBLE")
        return redirect("/")
    return render_template("page.html", result = output)

@app.route("/<bid>")
def beer(bid):
    beer = beers.get_beer(bid)
    brewery = beer['brewery']
    b = {}
    try:
        b['website'] = brewery['website'].encode('ascii', 'ignore')
    except:
        b['website'] = ""
    try:
        b['desc'] = brewery['description'].encode('ascii', 'ignore')
    except:
        b['desc'] = "No Brewery Description"
    try:    
        b['name'] = brewery['name'].encode('ascii', 'ignore')
    except:
        b['name'] = "No Brewery Name"
    try:    
        link = "https://www.google.com/maps/embed/v1/directions?key=AIzaSyBUxoapZRqwjQWrM0MFtM9wIf2NXFhX3Jo&origin=Stuyvesant+High+School&destination=" + urllib.quote_plus(brewery['locations'][0]['streetAddress'])
    except:
        link = "---"

    return render_template("beer.html", result = beer, brewery = b, link = link);

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4321)
