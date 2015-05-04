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

    place=query_result.places[0]
    place.get_details()
    result={}
    result['name']=elem['name']
    result['address']=place.formatted_address
    result['international_phone_number']=place.international_phone_number
    result['local_phone_number']=place.local_phone_number
    if place.website:
        result['website']=place.website
    result['geo_location']={'lat':place.geo_location['lat'],'lon':place.geo_location['lng']}
    result['google_url']=place.url
    result['google_maps_id']=place.place_id
    result['activity_types']=['ski','snowboard']
    specialized={}
    for attr in ["fast_eight", "beginner", "trails", "fast_sixes", "surface", "triple", "quad", "expert", "fast_quads", "longest_run", "trams", "lifts", "terrain_parks", "intermediate", "advanced", "double"]:
        if not elem.has_key(attr) or elem[attr] == '':
            continue
        #print attr,elem[attr]
        specialized[attr]=int(elem[attr])

    for attr in ["drop", "summit", "base","skiable_area", "snow_making"]:
        if not elem.has_key(attr) or elem[attr] == '':
            continue
        #print attr,elem[attr]
        specialized[attr]=elem[attr]

    result['ski'] = specialized
    places.append(result)

with io.open(r'data\onthesnowplace.json','wb')  as f:
    jsonfile=json.dumps(places, sort_keys=True, indent=4)
    f.write(jsonfile)