from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

    
def Logout(req):
    logout(req)
    return redirect('/')

def Signup(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = UserCreationForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                messages.add_message(req, messages.ERROR, 'compelet all fileds and strong password')
        form = UserCreationForm()
        context = {
            'form' : form
        }
        return render(req, 'registration/signup.html',context=context)
    return redirect('/')

def Login(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'GET':
        form = AuthenticationForm()
        return render(req, 'registration/login.html', {'form': form})
    if req.method == 'POST':
        form = AuthenticationForm(request=req, data=req.POST)
        user = req.POST['username']
        password = req.POST['password']
        if '@' in user:
            username = User.objects.get(email=user.lower()).username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req,user)
                return HttpResponseRedirect(reverse('home:home'))
            else:
                messages.add_message(req, messages.ERROR, 'username/email or password is incorrect')
                return HttpResponseRedirect(reverse('accounts:login'))
        else:
            user = authenticate(username=user, password=password)
            if user is not None:
                login(req,user)
                return HttpResponseRedirect(reverse('home:home'))
            else:
                messages.add_message(req, messages.ERROR, 'username/email or password is incorrect')
                return redirect('/accounts')