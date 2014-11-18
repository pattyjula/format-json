'''NOTES: Pull table from Parse.com and format JSON for use in JavaScript. Better than the alternative of hardcoding your JSON values into a JavaScript.
LIMITATIONS: Must use Parse.com ID and REST API keys

#AUTHOR: Patty Jula

DATE: November 17, 2014'''
#
# Import modules
import json,httplib,urllib
#
connection = httplib.HTTPSConnection('api.parse.com', 443) # Must use this address and port
connection.connect()
jsonOut = "C:/GIS/json/output.json" # Storage for final json

# Connect to Parse table with ID and REST keys
connection.request('GET', '/1/classes/Posts', '', {
       "X-Parse-Application-Id": "yourappkey", # add your Parse app key
       "X-Parse-REST-API-Key": "apikey" # add your Parse API key

     })

response = json.loads(connection.getresponse().read()) # get the values from your Parse database
recordDict = {"results":[]} # create an empty dictionary to store your results
#Format each result in response for use in JavaScript
for result in response["results"]:
	# Pulling only the necessary fields from the Parse result
	bicyclistCount = str(result["bicyclistCount"])
	text = str(result["text"])
	lat = str(result["location"]["latitude"])
	lon = str(result["location"]["longitude"])
	date = str(result["createdAt"])[:10]
	record = "bicyclistCount :"  + '"%s"' % bicyclistCount
	record = {"bicyclistCount":bicyclistCount, "text": text, "Lat": lat, "Lon": lon, "date":date} # format each record from your Parse json file
	recordDict["results"].append(record) # append your values to the dict
	print record
	
with open(jsonOut, 'w') as outfile:

	# Output formatted json to outfile
	json.dump(recordDict, outfile)

connection.close() # Close connection
