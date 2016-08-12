from django.contrib import admin
from .models import Version, TestCase, Persona, Defect, TestCharter, TestGroup, TestResult

# Register your models here.
admin.site.register(Version)
admin.site.register(TestCase)
admin.site.register(TestCharter)
admin.site.register(TestGroup)
admin.site.register(Persona)
admin.site.register(Defect)
admin.site.register(TestResult)
