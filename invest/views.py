from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from . import services
from .models import Stock
#from .services import get_featured_stocks
from django.contrib import messages
from .forms import StockForm
import json, requests
from django.contrib.admin.views.decorators import staff_member_required




# Create your views here.


def stock_detail_view(request):
    if request.method == 'POST':
        ticker = request.POST['ticker'].upper()
        response = services.make_request2(ticker)

        logo_response = services.get_logo(ticker)
        #financials_response = services.get_financials(ticker)

        try: 
            ### not working
            data = response.json()
            #data = json.loads(response.text)
            ###
            logo_data = logo_response.json()
            #financials_data = financials_response.json()


            companyName = data[ticker]['company']['companyName']
            price = data[ticker]['quote']['latestPrice']
            change = data[ticker]['quote']['change']
            changePercent = '{:,.2f}%'.format(data[ticker]['quote']['changePercent']*100)
            marketCap = "${:,.2f}".format(data[ticker]['quote']['marketCap']/1000000000)
            ytdChange = '{:,.2f}%'.format(data[ticker]['quote']['ytdChange']*100) 
            description = data[ticker]['company']['description']
            quote = data[ticker]['quote']
            peRatio = "{:,.2f}".format(data[ticker]['quote']['peRatio'])
            week52High = "${:,.2f}".format(data[ticker]['quote']['week52High'])
            week52Low = "${:,.2f}".format(data[ticker]['quote']['week52Low'])
            company = data[ticker]['company']
            news = data[ticker]['news']

            #financials = financials_data[ticker]['financials']
            logo_url = logo_data


        except Exception as e:
            print('an exception happened')
            print(data)
            data = 'error'

        return render(request, 'detail.html',{
                'data':data,
                'companyName':companyName,
                'price': price,
                'change': change,
                'changePercent': changePercent,
                'marketCap': marketCap,
                'ytdChange': ytdChange,
                'description': description,
                'peRatio':peRatio,
                'week52High':week52High,
                'week52Low':week52Low,

                'company': company,
                'quote':quote,
                'news':news,

                'logo':logo_url,
                
                })
    else:
        return render(request, 'detail.html',{'ticker':'Enter something'})


                

#--------------------------------------------------------------------

def list_view(request):   #add_stock
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            
            form.save()
            messages.success(request, 'Stock Has Been Added!')
            return redirect('list_view')
    else:
        ticker = Stock.objects.all().values_list()
        
        response = services.make_request2(ticker)

        try: 
            data = response.json()
            alist = []
            blist = []
            for i in data:
                testing = data[i]['quote']
                alist.append(testing)
                '''
                companyName = data[i]['company']['companyName']
                price = data[i]['quote']['latestPrice']
                change = data[i]['quote']['change']
                changePercent = '{:,.2f}%'.format(data[i]['quote']['changePercent']*100)
                marketCap = "${:,.2f}".format(data[i]['quote']['marketCap']/1000000000)
                ytdChange = '{:,.2f}%'.format(data[i]['quote']['ytdChange']*100) 
                description = data[i]['company']['description']
                '''
                testing2 = data[i]
                blist.append(testing2)


        except Exception as e:
            data = 'Error'

    context = {
            'ticker': ticker,
            'data' : data,
            'alist':alist,
            'blist':blist,
        }   
    return render(request, 'list_view.html', context)


#--------------------------------------------------------------------

def featured(request):  

    ticker = Stock.objects.all().featured().values_list()

    response = services.make_request2(ticker)

    try: 
        data = response.json()
        alist = []
        blist = []
        for i in data:
            testing = data[i]['quote']
            alist.append(testing)
            testing2 = data[i]
            blist.append(testing2)
            
    except Exception as e:
        data = 'Error'

    context = {
            'ticker': ticker,
            'data' : data,
            'alist':alist,
            'blist':blist,
            
        }   
    return render(request, 'featured.html', context)






def market_list(request):
    token = 'pk_95bc66cde9de469f99b40b52a5802fcd'
    api = 'https://cloud.iexapis.com/stable/stock/market/list/mostactive?token={}'.format(token)
    response = requests.get(api)
    try: 
        marketList = response.json()
        
    except Exception as e:
        marketList = 'Error'

    context = {
            'marketList' : marketList
        }   
    return render(request, 'featured.html', context)





def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ('Stock Has Been Deleted!'))
    return redirect(list_view)








'''
OLD STOCK WATCHLIST VIEW FROM SINGLE STOCK API CALL
---
CHANGED TO BATCH API
---
#@login_required
def watchlist2(request):   #add_stock
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            
            form.save()
            messages.success(request, 'Stock Has Been Added!')
            return redirect('watchlist')
    else:
        ticker = Stock.objects.all()
        
        output_quote = []
        output_company = []
        for ticker_item in ticker:

            response_quote = services.make_request(str(ticker_item))[0]
            response_company = services.make_request(str(ticker_item))[1]
            try: 
                data_quote = response_quote.json()
                data_company = response_company.json()

                output_quote.append(data_quote)
                output_company.append(data_company)

            except Exception as e:
                data_quote = 'Error'
                data_company = 'Error'

        context = {
                'ticker': ticker,
                'output_quote' : output_quote,
                'output_company' : output_company
            }   
        return render(request, 'watchlist.html', context)

'''









'''
OLD STOCK DETAIL VIEW FROM SINGLE STOCK API CALL
---
CHANGED TO BATCH API
---
def stock_old_view(request): #home  #single stock api call #NA

    if request.method == 'POST':
        ticker = request.POST['ticker']
        response_quote = services.make_request(ticker)[0]
        response_company = services.make_request(ticker)[1]
        try: 
            data_quote = response_quote.json()
            data_company = response_company.json()

            companyName = data_company['companyName']
            price = data_quote['latestPrice']
            change = data_quote['change']
            changePercent = '{:,.2f}%'.format(data_quote['changePercent']*100)
            marketCap = "${:,.2f}".format(data_quote['marketCap']/1000000000)
            ytdChange = '{:,.2f}%'.format(data_quote['ytdChange']*100) 
            description = data_company['description']

        except Exception as e:
            data_quote = 'Error'
            data_company = 'Error'
            
        return render(request, 'detail.html',{
                'data_quote' : data_quote,
                'data_company' : data_company,
                'companyName' : companyName,
                'price': price,
                'change': change,
                'changePercent': changePercent,
                'marketCap': marketCap,
                'ytdChange': ytdChange
            } )
    else:
        return render(request, 'detail.html',{'ticker':'Enter something'})
'''