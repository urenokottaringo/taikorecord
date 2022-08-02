from django.contrib import admin
from myapp.models import Director, Movie, Log 

admin.site.register(Director)
admin.site.register(Movie)       
admin.site.register(Log)