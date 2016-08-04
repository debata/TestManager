from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Version(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=None, blank=True)

    def __str__(self):
        return str(self.number) + ' - ' + self.name

class Persona(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=None)
    def __str__(self):
        return self.name

class TestCase(models.Model):
    versions = models.ManyToManyField(Version)
    priority = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    prerequisites = models.CharField(max_length=50, blank=True)
    persona = models.ForeignKey(Persona)
    procedure =  models.TextField(max_length=None)
    author = models.ForeignKey(User)
