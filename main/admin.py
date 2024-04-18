from django.contrib import admin

from main.models import Car, Client, Sale

admin.site.register([Car, Client, Sale])

