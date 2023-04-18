from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req, 'home/index.html')

def about(req):
    return render(req, 'home/about.html')

def contact(req):
    return render(req, 'home/contact.html')