from django.shortcuts import render
from .models import Course

# Create your views here.


def course(req):
    course = Course.objects.filter(status=True)
    context = {
        'course' : course
    }
    return render(req, 'course/courses.html', context=context)