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
    priority = models.CharField(max_length=15, choices=[('Critical', 'Critical'),('High', 'High'),('Medium', 'Medium'),('Low','Low')])
    name = models.CharField(max_length=50)
    prerequisites = models.CharField(max_length=50, blank=True)
    persona = models.ForeignKey(Persona)
    procedure =  models.TextField(max_length=None)
    author = models.ForeignKey(User)

    def __str__(self):
        return str(self.id) + ' - ' + self.name

class Defect(models.Model):
    name = models.CharField(max_length=50)
    description =  models.TextField(max_length=None)
    status = models.CharField(max_length=15, choices=[('Open', 'Open'),('In-work', 'In-work'),('Fixed', 'Fixed'),('In-test','In-test'),('Closed','Closed')])
    priority = models.CharField(max_length=15, choices=[('Critical', 'Critical'),('High', 'High'),('Medium', 'Medium'),('Low','Low')])
    affected_versions = models.ManyToManyField(Version, related_name='affected_versions', blank=True)
    fixed_versions = models.ManyToManyField(Version, related_name='fixed_version', blank=True)
    procedure =  models.TextField(max_length=None)
    reporter = models.ForeignKey(User, related_name='reporter_user')
    assigned = models.ForeignKey(User, related_name='assigned_user', blank=True)
    affected_test_cases = models.ManyToManyField(TestCase, blank=True)


