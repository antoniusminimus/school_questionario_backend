from django.contrib import admin

# Register your models here.
from surveys.models import Survey

admin.site.register(Survey)
