import json
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

#get a beer based on alcohol content
def get_beers(abv):
    #grab the database info
    url = "http://api.brewerydb.com/v2/beers/?key=0c040a3ebf5d18acb0162c76cea5ebc9&abv=" + str(abv)
    request = urllib2.urlopen(url)
    resultstring = request.read()
    db = json.loads(resultstring)
    results = db["data"]
    beers = []

    for beer in results:
        entry = {}
        entry['name'] = beer['name'].encode('ascii', 'ignore')
        entry['id'] = beer['id'].encode('ascii', 'ignore')
        try:
            entry['desc'] = beer['description'].encode('ascii', 'ignore')
        except:
            entry['desc'] = "No description available."
        try:
            entry['style'] = beer['style']['name'].encode('ascii', 'ignore')
        except:
            entry['style'] = "No style type available."
        try:
            entry['styledesc'] = beer['style']['desc'].encode('ascii', 'ignore')
        except:
            entry['styledesc'] = "No style description available."
        beers.append(entry)

    return beers

def get_beer(bid):
    #grab the database info
    url = "http://api.brewerydb.com/v2/beer/" + bid + "?key=0c040a3ebf5d18acb0162c76cea5ebc9&withBreweries=Y"
    request = urllib2.urlopen(url)
    resultstring = request.read()
    db = json.loads(resultstring)
    results = db["data"]
    beer = {}
    beer['name'] = results['name'].encode('ascii', 'ignore')
    beer['id'] = results['id'].encode('ascii', 'ignore')
    beer['brewery'] = results['breweries'][0]
    return beer
