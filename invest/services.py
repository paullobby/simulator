from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
import requests
import time


#symbol_list = ['TSLA', 'GME', 'MGM','BBBY','SPG']
def make_request(ticker):
    #basics
    token = 'pk_95bc66cde9de469f99b40b52a5802fcd'
    prod_api = 'https://cloud.iexapis.com/stable'
    #sandbox_api = 'https://sandbox.iexapis.com/stable'

    #two kinds of apis
    company_call = '/stock/{}/company'.format(ticker)
    quote_call = '/stock/{}/quote/'.format(ticker)

    #complete urls
    quote_url = '{}{}?token={}'.format(prod_api, quote_call, token)
    company_url = '{}{}?token={}'.format(prod_api, company_call, token)
    #url = 'https://finnhub.io/api/v1/quote?&symbol={}&token={}'.format(ticker,token)
    
    #make requests
    response_quote = requests.get(quote_url)
    response_company = requests.get(company_url)
    return response_quote, response_company


def make_request2(ticker):
    token = 'pk_95bc66cde9de469f99b40b52a5802fcd'
    q = 'quote'
    c = 'company'
    n = 'news'
    api = 'https://cloud.iexapis.com/stable/stock/market/batch?symbols={}&types={},{},{}&token={}'.format(ticker, q, c, n, token)
    response = requests.get(api)
    return response

def get_logo(ticker):
    token = 'pk_95bc66cde9de469f99b40b52a5802fcd'
    api1 = 'https://cloud.iexapis.com/stable/stock/{}/logo?token={}'.format(ticker, token)
    response1 = requests.get(api1)
    return response1

'''
def get_financials(ticker):
    token = 'pk_95bc66cde9de469f99b40b52a5802fcd'
    api2 = 'https://cloud.iexapis.com/stable/stock/{}/financials?token={}'.format(ticker, token)
    response2 = requests.get(api2)
    return response2

'''











'''
def get_featured_stocks(stock):
        
    ticker = stock.symbol
    response_quote = make_request(ticker)[0]
    response_company = make_request(ticker)[1]


    data_quote = response_quote.json()
    data_company = response_company.json()
    
    price = data_quote['latestPrice']
    change = data_quote['change']
    changePercent = '{0:0f}%'.format(data_quote['changePercent']*100)
    description = data_company['description']
    companyName = data_company['companyName']

    record = {
        'Symbol' : ticker,
        'Company' : companyName,
        'Price' : price,
        'Change' : change,
        'ChangePercent' : changePercent,
        'Description' : description
    }
    print(record)
    return record
'''

















