from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.


def course(req):
    course = Course.objects.filter(status=True)
    context = {
        'course' : course
    }
    return render(req, 'course/courses.html', context=context)

def course_detail(req, pid=None):
    course = get_object_or_404(Course,pk=pid)
    course.counted_views += 1
    course.save()
    context = {
        'course' : course
    }
    return render(req, 'course/course-details.html', context=context)
