from django.http import *
from django.http import HttpResponse
from django.template import RequestContext
from ElasticSearch.Esearch import ES_query
from django.shortcuts import render
from .models import SportType
from django.shortcuts import render_to_response
import socket
import json

def ajax_test(request):
    if request.method == 'POST':
        if 'sportsType' in request.POST:
            sports_type = request.POST['sportsType']
            return HttpResponse("Success!!!") #tried without the json. Doesn't work either

    return render(request, 'search/index.html')

def index(request):
    sportType = SportType.objects.all()
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
        to_search = request.POST['Court_Name']
        q = ES_query()
        hits = q.q_place(to_search)
        output = []
        for i in range(min(10,len(hits))):
            temp = 'rank: ' + str(i+1)
            stadium = hits[i]["_source"]
            temp = temp + '     name: ' + stadium['name'][0]
            output.append(temp)
        return render(request,'search/index.html',{'hits':hits,'output':output})
    else:
        return HttpResponse("Nothing found");

