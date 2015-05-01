from googleplaces import GooglePlaces, types, lang
import json

YOUR_API_KEY = 'AIzaSyCTqay66rwdaS5CdL9C2BArgrh5Xxwprfs'
    #'AIzaSyDWvbupdPsaDcbzBsEjc7El5QYDu6eregc'
    #'AIzaSyAROXFHSbtR0OA1hNKP8VaBRaUzUegksPA'

google_places = GooglePlaces(YOUR_API_KEY)

# cities = []
skiplaces=json.load(r'../data/onthesnow.json')
for elem in skiplaces:
    query_result = google_places.text_search(
    query= elem.name)


    #if query_result.has_attributions:
     #   print query_result.html_attributions
    #print query_result
    print elem.name
    for place in query_result.places:
        place.get_details()
        print place.name
        #print place.geo_location
        #print place.place_id

        badminton[place.place_id] = place.details

json.dumps(badminton, sort_keys=True, indent=4)