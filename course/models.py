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

class Course(models.Model):
    image = models.ImageField(upload_to = 'course', default= 'default.jpg')
    name = models.CharField(max_length=120)
    detaits = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    category = models.ManyToManyField(category)
    level_course = models.ManyToManyField(level)

    class Meta:

        ordering = ['-created_date']

    def __str__(self):
        return self.name

# Create your models here.
