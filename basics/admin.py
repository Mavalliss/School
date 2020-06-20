from django.contrib import admin
from .models import News, Urgent

# Register your models here.

admin.site.register(News)
admin.site.register(Urgent)
