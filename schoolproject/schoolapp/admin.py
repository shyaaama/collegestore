from django.contrib import admin

# Register your models her
from django.contrib import admin

# Register your models here.
from .models import Course, Department, Person

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Person)

