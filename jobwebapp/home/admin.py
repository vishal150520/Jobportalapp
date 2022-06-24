from django.contrib import admin

# Register your models here.
from .models import candidate
from .models import company
admin.site.register(company)
admin.site.register(candidate)