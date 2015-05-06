from django.http import *
from django.http import HttpResponse
from django.template import RequestContext
from ElasticSearch.Esearch import ES_query
from django.shortcuts import render
from .models import SportType
<<<<<<< HEAD
from django.shortcuts import render_to_response
import socket
import json
from search.toGolocation import to_golocation
||||||| merged common ancestors
=======
from django.shortcuts import render_to_response
import socket
import json

def ajax_test(request):
    if request.method == 'POST':
        if 'sportsType' in request.POST:
            sports_type = request.POST['sportsType']
            return HttpResponse("Success!!!") #tried without the json. Doesn't work either

    return render(request, 'search/index.html')
>>>>>>> origin/master

def index(request):
    sportType = SportType.objects.all()
<<<<<<< HEAD
    if 'Court_Name' in request.POST and 'selectedType' in request.POST:
||||||| merged common ancestors
    return render(request,'search/index.html',{'sportType':sportType})


def search_result(request):
    if 'Court_Name' in request.POST:
=======
    if request.is_ajax():
        if 'selectedType' in request.POST:
            selectedType = request.POST['selectedType']
            print selectedType
            return render(request,'search/index.html',{'selectedType':selectedType})
        return HttpResponse("Success!!!")
    else:
        if 'Court_Name' in request.POST:
            to_search = request.POST['Court_Name']
            q = ES_query()
            hits = q.q_place(to_search)
            output = []
            for i in range(min(10,len(hits))):
                temp = 'rank: ' + str(i+1)
                stadium = hits[i]["_source"]
                temp = temp + '     name: ' + stadium['name'][0]
                output.append(temp)
            return render(request,'search/index.html',{'hits':hits,'output':output,'sportType':sportType, 'searchText': to_search})
        else:
            return render(request,'search/index.html',{'sportType':sportType})


def search_result(request):
    if 'Court_Name' in request.POST:
>>>>>>> origin/master
        to_search = request.POST['Court_Name']
        selectedType = request.POST['selectedType']
        location = to_golocation(to_search)
        lat = location['lat']
        lng = location['lng']
        q = ES_query()
        hits = q.q_mwf(selectedType.lower(),lat,lng)
        output = []
        for i in range(min(10,len(hits['hits']['hits']))):
            res = hits['hits']['hits']
            temp = 'rank: ' + str(i+1)
            stadium = res[i]["_source"]
            temp = temp + '     name: ' + stadium['name']
            output.append(temp)
<<<<<<< HEAD
        print len(output)
        return render(request,'search/index.html',{'sportType':sportType, 'searchText':to_search,'output':output})
||||||| merged common ancestors
        return render(request,'search/search_result.html',{'hits':hits,'output':output})
=======
        return render(request,'search/index.html',{'hits':hits,'output':output})
>>>>>>> origin/master
    else:
        return render(request,'search/index.html',{'sportType':sportType})



