from django.contrib import admin

from .models import *


class CourseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','teacher', 'status', 'published_date')
    list_filter = ('status', )
    search_fields = ('name', 'teacher' )
    empty_value_display = '-empty-'
admin.site.register(Course, CourseAdmin)
admin.site.register(category)
admin.site.register(level)
admin.site.register(skills)
admin.site.register(RegisterUser)