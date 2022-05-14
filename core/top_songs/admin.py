from django.contrib import admin

# Register your models here.
from .models import Track, Artist, Genre

'''Models register in Django-Admin site'''

admin.site.register([Track, Artist, Genre])
