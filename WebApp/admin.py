from django.contrib import admin

# Register your models here.
from WebApp.models import Users

class UsersAdmin(admin.ModelAdmin):
    list_display = ['EmpId','EmpName','EmpId','EmpAge','Photo','resume']

admin.site.register(Users,UsersAdmin)