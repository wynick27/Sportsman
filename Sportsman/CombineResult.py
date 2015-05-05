from googleplaces import GooglePlaces, types, lang
import json
import io
import sys, codecs
# set up output encoding
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

YOUR_API_KEY = 'AIzaSyCTqay66rwdaS5CdL9C2BArgrh5Xxwprfs'
    #'AIzaSyDWvbupdPsaDcbzBsEjc7El5QYDu6eregc'
    #'AIzaSyAROXFHSbtR0OA1hNKP8VaBRaUzUegksPA'

google_places = GooglePlaces(YOUR_API_KEY)

places = []
skiplaces=json.load(open(r'data\onthesnow.json','r'))
for elem in skiplaces:
    query_result = google_places.text_search(
    query= elem['name'])


    #if query_result.has_attributions:
     #   print query_result.html_attributions
    #print query_result
    print elem['name']
    for place in query_result.places:
        place.get_details()
        print place.name
        #print place.geo_location
        #print place.place_id
        
        places.append(place.details)

json.dump(places,io.open(r'data\onthesnowplace.json','w',encoding='utf-8'), sort_keys=True, indent=4)