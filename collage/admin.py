from django.contrib import admin

from .models import Department,Student

admin.site.register(Department)
admin.site.register(Student)
# admin.site.register(Subject)