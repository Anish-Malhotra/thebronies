from flask import Flask, render_template, request
from random import randint
import urllib2, json, random

app = Flask(__name__)

german = ["l8Qtgj", "Hbpi1r", "dadokQ"]
british = ["3XfZXX", "c6Ke7P", "iaIlts"]
belgian = ["fdnFoV", "5yCG1U", "ynIdkL"]
french = ["1wSztN", "QyT3s1", "j1V1eo"]
beers = [german, british, belgian, french]

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        button = request.form["b"]
        if button == None:
            return render_template("home.html")
        else:
            place = random.choice(beers)
            search = random.choice(place)
            return page(search)

@app.route("/")
def page(search=None):
    #get a random beer
    url = "http://api.brewerydb.com/v2/beer/" + search + "/?key=0c040a3ebf5d18acb0162c76cea5ebc9"
    request = urllib2.urlopen(url)
    resultstring = request.read()
    d = json.loads(resultstring)
    name = d["data"]["name"]
    try:
        desc = d["data"]["description"]
    except:
        desc = "No description."
    try:
        abv = d["data"]["abv"]
    except:
        abv = "N/A"
    info = [name.encode('ascii', 'ignore'), 
            desc.encode('ascii', 'ignore'), 
            abv.encode('ascii', 'ignore')]
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
    output = [info, 
              link.encode('ascii', 'ignore')]
    return render_template("page.html", result = output)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4321)

