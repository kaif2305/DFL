from django.contrib.auth import forms
from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from.models import *

class CreateRegDonarForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','email','password1','password2']
        

class RequestForm(ModelForm):
    class Meta:
        model = Requests
        fields = ('item_name_id', 'quantity', 'amount')
        
        