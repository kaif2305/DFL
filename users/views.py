from django.shortcuts import render, redirect
from django.http import HttpResponse, request, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from.forms import *
from . models import*
# Create your views here.
  
def loginasdonar(request):
    if request.user.is_authenticated :
        return redirect('donate-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('donate-home')
            else:
                messages.info(request, 'Username OR Password is incorrect')
                
        return render(request, 'DFL/Login_donar.html')

def logoutdonar(request):
    logout(request)
    return redirect('donate-login')

def registerasdonar(request):
    if request.user.is_authenticated :
        return redirect('donate-home')
    else:
        form = CreateRegDonarForm()
        
        if request.method  == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save() 
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                
                return redirect('donate-login')
        return render(request, "DFL/Register_donar.html", {"form": form})
  
@login_required(login_url = 'donate-login')
def home(request):
    return render(request, 'DFL/index.html')

def saverequest(request):
    if request.method =='POST':
        itemname = request.POST.get('itemname')
        quantity = request.POST.get('quantity')
        amount = request.POST.get('amount')
        data = requestitems(itemname = itemname, quantity = quantity, amount = amount)
        data.save()
    return render(request, 'DFL/donateButton.html')
@login_required(login_url = 'donate-login')   
def donate(request):
    donates = To_Donate.objects.all()
    return render(request, 'DFL/donateButton.html',{'donates': donates})

@login_required(login_url = 'donate-login')
def deliver(request):
    return render(request, 'DFL/deliver.html')

@login_required(login_url = 'donate-login')
def team(request):
    return render(request, 'DFL/Our-Team.html')

@login_required(login_url = 'donate-login')
def contact(request):
    return render(request, 'DFL/contact.html')


#organisation

def loginasorg(request):
    if request.user.is_authenticated :
        return redirect('org-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('org-home')
            else:
                messages.info(request, 'Username OR Password is incorrect')
                
        return render(request, 'DFL/Login_org.html')
 
@login_required(login_url = 'org-login')   
def logoutorg(request):
    logout(request)
    return redirect('org-login')

@login_required(login_url = 'org-login')
def registerasorg(request):
    if request.user.is_authenticated :
        return redirect('org-home')
    else:
        form = CreateRegDonarForm()
        
        if request.method  == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save() 
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                
                return redirect('org-login')
        return render(request, "DFL/Register_org.html", {"form": form})
  
@login_required(login_url = 'org-login')
def org_home(request):
    return render(request, 'DFL/indexorg.html')
    
@login_required(login_url = 'org-login')    
def resources(request):
    resource = Resources.objects.all()
    return render(request, 'DFL/Resources.html', {'resource': resource})
    
@login_required(login_url = 'org-login')    
def Request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
    req = Requests.objects.all()
    return render(request, 'DFL/Request.html',{'form': form, 'req': req} )

# def requestform(request):
#     form = RequestForm()
#     return render(request, 'DFL/Request.html', {'form': form} )


@login_required(login_url = 'org-login')
def team_org(request):
    return render(request, 'DFL/Our-Teamorg.html')

@login_required(login_url = 'org-login')
def contact_org(request):
    return render(request, 'DFL/contactorg.html')
