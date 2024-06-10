from django.contrib import admin
from service.models import *
from django.contrib.auth.admin import UserAdmin

class ContactAdmin(admin.ModelAdmin):
    list_display=('username', 'email', 'message')
admin.site.register(Contact, ContactAdmin)

class AdddetailsAdmin(admin.ModelAdmin):
    list_display=('student_name', 'branch', 'yop')
admin.site.register(Add_Details, AdddetailsAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=('first_name', 'lastname', 'gender', 'date_of_birth', 'marital_status', 
        'email', 'phonenumber', 'add', 'course')
admin.site.register(Course, CourseAdmin)

# Register your models here.
