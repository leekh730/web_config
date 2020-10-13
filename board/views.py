from django.shortcuts import render
from pymongo import MongoClient
import requests

# Create your views here.
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://192.168.219.124:27017/') as client:
        mydb = client.mydb
        result = list(mydb.economic.find({}))
        data['page_obj'] = result
    return render(request, 'board/listwithmongo.html', context=data)
