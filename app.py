from flask import Flask
import urllib2
import json

app = Flask(__name__)

url = """
http://api.brewerydb.com/v2/beer/?key=<MYKEY>&format=json
"""

url1 ="""
http://api.brewerydb.com/v2/location/d25euf/?key=0c040a3ebf5d18acb0162c76cea5ebc9
"""

url2 ="""
http://ponyfac.es/api.json/tag:happy
"""


@app.route("/")
def home():
    request = urllib2.urlopen(url1)
    resultstring = request.read()
    result = json.loads(resultstring)
    return resultstring
   # return str(result["timestamp"])

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4321)

