from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/<str:pk>/', views.dashboard, name='dashboard'),
    path('quote/<str:pk>/', views.quote, name='quote'),
    path('trade/<str:pk>/', views.trade, name='trade'),
    path('buy/<str:pk>/<str:symbol>/', views.buy, name='buy'),
    path('sell/<str:pk>/<str:symbol>/', views.sell, name='sell'),
    path('settings/<str:pk>/', views.settings, name='settings'),
    path('trade-history/<str:pk>/', views.trade_history, name='trade_history'),
]