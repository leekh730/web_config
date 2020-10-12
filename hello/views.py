from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hello(request):
    return HttpResponse("Hello, Django!")

def home(request):
    return render(request, 'home.html')

# def responsewithhtml(request):
#     data = {'first':'Kunhee', 'second':'Lee'}
#     return render(request, 'hello/responsewithhtml.html', context=data)

def form(request):
    return render(request, 'hello/requestform.html')

def responsewithhtml(request):
    data = dict()
    data['first'] = request.GET['first']; data['second'] = request.GET['second']
    return render(request, 'hello/responsewithhtml.html', context=data)
