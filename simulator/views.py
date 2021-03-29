from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from invest.models import Stock
from invest import services
import requests


def home(request):
    return render(request, 'index.html')


def user_guide(request):
    return render(request, 'user_guide.html')

def best_practices(request):
    return render(request, 'best_practices.html')



def home_list(request):
    token = 'pk_95bc66cde9de469f99b40b52a5802fcd'
    api = 'https://cloud.iexapis.com/stable/stock/market/list/mostactive?token={}'.format(token)
    response = requests.get(api)
    try: 
        data = response.json()
        print(data)
        
    except Exception as e:
        data = 'Error'

    context = {
            'data' : data
        }   
    return render(request, 'index.html', context)