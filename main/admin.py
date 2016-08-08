from django.contrib import admin
from .models import Version, TestCase, Persona, Defect

# Register your models here.
admin.site.register(Version)
admin.site.register(TestCase)
admin.site.register(Persona)
admin.site.register(Defect)
