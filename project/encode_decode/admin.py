from django.contrib import admin
from .models import decodeFile, encodeFile

admin.site.register(decodeFile)
admin.site.register(encodeFile)

# Register your models here.
