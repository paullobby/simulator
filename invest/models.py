from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


#Model Manager

class StockQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

class StockManager(models.Manager):
    def get_queryset(self):
        return StockQuerySet(self.model, using=self._db)

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs= self.get_queryset().filter(id=id)   
        if qs.count()==1:
            return qs.first()
        return None



class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    #name = models.CharField(max_length=100)
    featured   = models.BooleanField(default=False)
    user        =models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    objects = StockManager()

    def __str__(self):
        return self.ticker

    def __unicode__(self):
        return self.ticker

