from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import CaptchaForm

    
def Logout(req):
    logout(req)
    return redirect('/')

def Signup(req):
#    if req.method == 'POST':
#        captcha = CaptchaForm(req.POST)
#        if captcha.is_valid():
#            pass
#        else:
#            captcha = CaptchaForm()
#            form = UserCreationForm()
#            messages.add_message(req, messages.ERROR, 'captcha is incorrect')
#            return render(req, 'registration/signup.html', {'form': form, 'captcha': captcha})
#        
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return render (req, 'home/down.html')
        else:
            messages.add_message(req, messages.ERROR, '...! لطفا تمام فیلد ها را کامل و یا پسوردی قوی تر انتخاب نمایید ')
    form = UserCreationForm()
    context = {
        'form' : form,
        }
    return render(req, 'registration/signup.html',context=context)

def Login(req):
    if req.method == 'POST':
        captcha = CaptchaForm(req.POST)
        if captcha.is_valid():
            pass
        else:
            captcha = CaptchaForm()
            form = AuthenticationForm()
            messages.add_message(req, messages.ERROR, 'کد امنیتی صحیح نمیباشد')
            return render(req, 'registration/login.html', {'form': form, 'captcha': captcha})

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
                messages.add_message(req, messages.ERROR, 'نام کاربری یا کلمه عبور اشتباه است')
        else:
            user = authenticate(username=user, password=password)
            if user is not None:
                login(req,user)
                return HttpResponseRedirect(reverse('home:home'))
            else:
                messages.add_message(req, messages.ERROR, 'نام کاربری یا کلمه عبور اشتباه است')
    
    form = AuthenticationForm()
    captcha = CaptchaForm()
    return render(req, 'registration/login.html', {'form': form, 'captcha': captcha})