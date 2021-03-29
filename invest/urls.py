from django.urls import path, include
from . import views
from .views import list_view, stock_detail_view, featured

urlpatterns = [
    path('featured/', featured, name='featured'),
    path('detail/', stock_detail_view, name='detail'),
    path('list_view/', views.list_view, name='list_view'),
]
