from django.shortcuts import render
from pymongo import MongoClient
import requests
from django.core.paginator import Paginator

# Create your views here.
def listwithmongo(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client: # use my ip and sync with datas/scrapingandinsertmongo.py
        mydb = client.mydb
        result = list(mydb.economic.find({}))
        data['page_obj'] = result
    return render(request, 'board/listwithmongo.html', context=data)

def listwithmongowithpaginator(request):
    data = request.GET.copy()
    with MongoClient('mongodb://127.0.0.1:27017/') as client:
        mydb = client.mydb
        contact_list = list(mydb.economic.find({}))
    paginator = Paginator(contact_list, 10) # 1 페이지에 10개의 자료를 보여라
    page_number = request.GET.get('page',1)
    data['page_obj']=paginator.get_page(page_number)
    return render(request, 'board/listwithmongowithpaginator.html', context=data)
