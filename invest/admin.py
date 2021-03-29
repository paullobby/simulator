from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Stock







class StockAdmin(admin.ModelAdmin):
    search_fields = ['symbol']
    class Meta:
        model = Stock
        ordering = ['ticker']

admin.site.register(Stock)

