from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse
from .forms import changeform,userform,warningform
# from django.contrib.auth.models import User

# Create your views here.
def observation(request):
    if request.method == "POST":
        form = warningform(request.POST)
        if form.is_valid():
            Tphase1 = form.cleaned_data.get('Tphase1')
            Tphase2 = form.cleaned_data.get('Tphase2')
            Pphase1 = form.cleaned_data.get('Pphase1')
            Pphase2 = form.cleaned_data.get('Pphase2')
            peoplenumber = form.cleaned_data.get('peoplenumber')
            staytime = form.cleaned_data.get('staytime')
            if staytime < Tphase1:
                phase = 'phase1'
            elif Tphase1 <= staytime and staytime <= Tphase2:
                phase = 'phase2'
            else:
                phase = 'phase3'

            return render(request,'observation.html',{'phase':phase})
    else:
        form = warningform()
    return render(request, 'observation.html',{'form': form})

def change_password(request):
    if request.method == "POST":
        form = changeform(request.POST)
        if form.is_valid():
            Username = request.user.username
            Oldpassword = form.cleaned_data.get('Oldpassword')
            Newpassword = form.cleaned_data.get('Newpassword')
            Confirmpass = form.cleaned_data.get('Confirmpass')
            user = auth.authenticate(username=Username, password=Oldpassword)
            if user is not None and Confirmpass == Newpassword:
                user.set_password(Newpassword)
                user.save()
                return redirect('/')
            else:
                message = 'Oldpassword is wrong or new password is different'
                return render(request,'change_password.html',{'message':message})
    else:
        form = changeform()
        return render(request, 'change_password.html', {'form': form})
    
def add_user(request):  
    if request.method == 'POST':
        form = userform(request.POST)  
        if form.is_valid():
            Username = form.cleaned_data['Username']
            Password = form.cleaned_data['Password']
            Confirmpass = form.cleaned_data['Confirmpass']
            if User.objects.filter(username=Username) or Confirmpass != Password:
               message = 'Username already exists or password is different'
               return render(request, 'add_user.html',{'message':message})

            user = User.objects.create_user(username=Username, password=Password)
            user.save()
            return redirect('/')    
    else:
        form = UserCreationForm()
    return render(request, 'add_user.html',{'form': form})


