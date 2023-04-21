from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.


def course(req, ctgr=None, teacher=None):
    course = Course.objects.filter(status=True)
    if ctgr:
        course = course.filter(category__name=ctgr)
    
    if teacher:
        course = course.filter(teacher__username=teacher)
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


def register(req):
    if req.method == 'GET':
        form = RegisterForm()
        return render(req, 'course/register.html', {'form': form})
    elif req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            messages.add_message(req, messages.SUCCESS, 'REGISTER SUCCESSFULL : call with you as soon')
            return redirect('/course/')
        
