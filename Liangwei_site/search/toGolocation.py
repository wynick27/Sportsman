__author__ = 'guoliangwei'
from googleplaces import GooglePlaces, types, lang
import sys, codecs

def to_golocation(tosearch):

    YOUR_API_KEY = 'AIzaSyCTqay66rwdaS5CdL9C2BArgrh5Xxwprfs'
        #'AIzaSyDWvbupdPsaDcbzBsEjc7El5QYDu6eregc'
        #'AIzaSyAROXFHSbtR0OA1hNKP8VaBRaUzUegksPA'

    google_places = GooglePlaces(YOUR_API_KEY)

    query_result = google_places.text_search(query=tosearch)
    if len(query_result.places) >= 1:
        place = query_result.places[0]
        place.get_details()
        return place.geo_location
    else:
        return None

if __name__ == '__main__':
    print to_golocation('57 Vernon St,Waltham, MA')



