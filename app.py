from flask import Flask
import urllib2
import json

app = Flask(__name__)

url = """http://ponyfac.es/api.json/tag:happy"""

@app.route("/")
def home():
    request = urllib2.urlopen(url)
    resultstring = request.read()
    result = json.loads(resultstring)
    return result

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=1000)

