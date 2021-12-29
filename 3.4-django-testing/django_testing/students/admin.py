from django.contrib import admin
from .models import Course, Student

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name']