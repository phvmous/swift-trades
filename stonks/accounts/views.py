from django.shortcuts import render
from .models import *
from .constants import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('home')

def dashboard(request, pk):
    user = User.objects.get(id=pk)
    trades = user.trade_set.all()
    total_trades = trades.count()
    positions = user.stock_set.all()
    total_positions = positions.count()
    
    # get balance
    balance = 0
    for position in positions:
        quote = getQuote(position.symbol)
        position.price = quote['price']
        position.save()
        balance += float(position.price * position.shares)
    balance = f'{balance:,.2f}'
    
    context = {
        'sitename': SITENAME,
        'user': user,
        'total_trades': total_trades,
        'total_positions': total_positions,
        'balance': balance,
        'trades': trades,
        'positions': positions,
    }
    return render(request, 'accounts/dashboard.html', context)


def quote(request, pk):
    return HttpResponse('quote')


def trade(request, pk):
    return HttpResponse('trade')
    

def buy(request, pk, symbol):
    return HttpResponse('buy')


def sell(request, pk, symbol):
    return HttpResponse('sell')


def trade_history(request, pk):
    return HttpResponse('trade_history')


def settings(request, pk):
    return HttpResponse('settings')