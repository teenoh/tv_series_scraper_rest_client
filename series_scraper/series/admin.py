from django.contrib import admin
from .models import Series, Seasons, Episodes
# Register your models here.

admin.site.register(Series)
admin.site.register(Seasons)
admin.site.register(Episodes)