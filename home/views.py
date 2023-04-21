from django.shortcuts import render, redirect
from course.models import Course
from django.contrib.auth.models import User
from .models import my_services
from .forms import NewsletterForm, ContactusForm

# Create your views here.


def home(req):
    if req.method == 'GET':
        email = NewsletterForm()
        services = my_services.objects.all()
        teacher_count = Course.objects.values_list('teacher').count()
        user_count = User.objects.all().count()
        course_count = Course.objects.all().count()
        course = Course.objects.all()[:2]
        context = {
            'teacher_count' : teacher_count,
            'user_count' : user_count,
            'course_count' : course_count,
            'course' : course,
            'services' : services,
            'email' : email,
        }
        return render(req, 'home/index.html', context=context)
    elif req.method == 'POST':
        form = NewsletterForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

def about(req):
    course = Course.objects.all()[:5]
    teacher_count = Course.objects.values_list('teacher').count()
    user_count = User.objects.all().count()
    course_count = Course.objects.all().count()
    context = {
        'teacher_count' : teacher_count,
        'user_count' : user_count,
        'course_count' : course_count,
        'course' : course,
    }
    return render(req, 'home/about.html', context=context)

def contact(req):
    if req.method == 'GET':
        form = ContactusForm()
        context = {
        'form' : form,
        }
        return render(req, 'home/contact.html', context=context)
    elif req.method == 'POST':
        form = ContactusForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact')
    