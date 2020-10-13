from django.shortcuts import render
from pymongo import MongoClient
import requests

# Create your views here.
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client: # use my ip and sync with datas/scrapingandinsertmongo.py
        mydb = client.mydb
        result = list(mydb.economic.find({}))
        data['page_obj'] = result
    return render(request, 'board/listwithmongo.html', context=data)
