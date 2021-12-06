from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User
# from django.db.models import Sum

class requestitems(models.Model):
    itemname = models.CharField(max_length=200,primary_key=True)
    quantity = models.FloatField( null=True)
    amount = models.FloatField( null=True)
        
class Requests(models.Model):
    item_name_id = models.CharField('Item Name',max_length=200,primary_key=True)
    quantity = models.FloatField( null=True)
    amount = models.FloatField( null=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.item_name_id

class To_Donate(models.Model):
    request = models.ForeignKey(Requests,null = True, on_delete= models.CASCADE )
    item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.FloatField( null=True)
    amount = models.FloatField( null=True) 
    
    def __str__(self):
        return self.donar_name
    
class Resources(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    donar_name = models.CharField(max_length=200, null=True)
    item_name = models.CharField(max_length=200, null=True)
    quantity = models.FloatField( null=True)
    amount = models.FloatField( null=True)
    doanted = models.ForeignKey(To_Donate, default = 1, on_delete= models.CASCADE )
    def __str__(self):
        return self.donar_name