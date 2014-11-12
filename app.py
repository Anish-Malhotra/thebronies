from flask import Flask, render_template, request
import urllib2, json

app = Flask(__name__)

url1 ="""
http://api.brewerydb.com/v2/location/d25euf/?key=0c040a3ebf5d18acb0162c76cea5ebc9
"""

url2 ="""
http://ponyfac.es/api.json/tag:happy
"""

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        search = request.form["search"]
        button = request.form["b"]
        if button == None:
            return render_template("home.html")
        else:
            return page(search)

@app.route("/")
def page(search=None):
    url = "http://api.brewerydb.com/v2/beer/" + search + "/?key=0c040a3ebf5d18acb0162c76cea5ebc9"
    request = urllib2.urlopen(url)
    resultstring = request.read()
    return render_template("page.html", result = resultstring)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4321)

