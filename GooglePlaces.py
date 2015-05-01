__author__ = 'CassyLee'

from googleplaces import GooglePlaces, types, lang
import json

YOUR_API_KEY = 'AIzaSyCTqay66rwdaS5CdL9C2BArgrh5Xxwprfs'

google_places = GooglePlaces(YOUR_API_KEY)

# cities = []
badminton = {}
g = open('cities.txt', 'r')
lines = g.readlines()
for city in lines:
    query_result = google_places.text_search(
    location= city,radius = 50000,query='badminton court')


    #if query_result.has_attributions:
     #   print query_result.html_attributions
    #print query_result
    print city
    for place in query_result.places:
        place.get_details()
        print place.name
        #print place.geo_location
        #print place.place_id

        badminton[place.place_id] = place.details

print len(badminton)
newfile = 'google_badminton.txt'
f = open(newfile, 'w')
f.write(json.dumps(badminton, sort_keys=True, indent=4))
f.close()
g.close()
        #print place.details  # A dict matching the JSON response from Google.

        #print '\n'



