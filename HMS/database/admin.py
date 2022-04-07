from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Hospital Management System"
admin.site.register(hr)
admin.site.register(receptionist)
