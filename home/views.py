from django.shortcuts import render
from course.models import Course
from django.contrib.auth.models import User

# Create your views here.


def home(req):
    teacher_count = Course.objects.values_list('teacher').count()
    user_count = User.objects.all().count()
    course_count = Course.objects.all().count()
    course = Course.objects.all()[:2]
    context = {
        'teacher_count' : teacher_count,
        'user_count' : user_count,
        'course_count' : course_count,
        'course' : course,
    }
    return render(req, 'home/index.html', context=context)

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
    return render(req, 'home/contact.html')