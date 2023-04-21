from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    
class level(models.Model):
    level = models.CharField(max_length=120)
    
    def __str__(self):
        return self.level

class skills(models.Model):
    teacher_skills = models.CharField(max_length=120)
    
    def __str__(self):
        return self.teacher_skills


class Course(models.Model):
    image = models.ImageField(upload_to = 'course', default= 'default.jpg')
    name = models.CharField(max_length=120)
    detaits = models.TextField()
    content = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_resume = models.TextField()
    price = models.IntegerField(default=0)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    category = models.ManyToManyField(category)
    level_course = models.ManyToManyField(level)
    skills = models.ManyToManyField(skills)
    available_sits = models.IntegerField(default=0)

    class Meta:

        ordering = ['-created_date']

    def __str__(self):
        return self.name

class RegisterUser(models.Model):
    name = models.CharField(max_length=120)
    family = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name
