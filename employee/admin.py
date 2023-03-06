# admin.py

from django.contrib import admin
from .models import User


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'address', 'profile_pic')
    list_display_links = ('id', 'username')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')
    list_per_page = 25


admin.site.register(User, EmployeeAdmin)


