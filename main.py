import urllib.request
import json

def printResault(data):
    JSONData = json.loads(data)
    if 'title' in JSONData["metadata"]:
        print(JSONData["metadata"]["title"])
    if 'count' in JSONData["metadata"]:
        print(JSONData["metadata"]["count"], "events are recorded!")
    if 'features' in JSONData:
        for index,feature in enumerate(JSONData["features"]):
            numOfPeople =0 if feature["properties"]["felt"] == None  else feature["properties"]["felt"] ;
            message = str(index+1) + " - " + \
                    feature["properties"]["place"]  \
                    + ", with mag = " \
                    + str(feature["properties"]["mag"])+" and " \
                    + str( numOfPeople) \
                    + " people felt it.";


            print(message)
           
def main():
    url="https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
    webUrl = urllib.request.urlopen(url)
    if(webUrl.getcode()==200):
        data =  webUrl.read()
        printResault(data)
    else:
        print("Connection Error!")


if __name__ == '__main__':
    main()
