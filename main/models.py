from django.db import models
from django.contrib.auth.models import User

priority_fields = [('Critical', 'Critical'),
                   ('High', 'High'),
                   ('Medium', 'Medium'),
                   ('Low', 'Low')]
test_states = [('Not Run', 'Not Run'), ('Pass', 'Pass'),
               ('Fail', 'Fail'), ('N/A', 'N/A')]
defect_states = [('Open', 'Open'), ('In-work', 'In-work'),
                 ('Fixed', 'Fixed'), ('In-test', 'In-test'),
                 ('Closed', 'Closed')]


# Create your models here
class Version(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=None, blank=True, null=True)

    def __str__(self):
        return str(self.number) + ' - ' + self.name


class Persona(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=None)

    def __str__(self):
        return self.name


class TestCase(models.Model):
    versions = models.ManyToManyField(Version)
    priority = models.CharField(
            max_length=15, choices=priority_fields)
    name = models.CharField(max_length=50)
    prerequisites = models.CharField(max_length=50, blank=True, null=True)
    persona = models.ForeignKey(Persona)
    procedure = models.TextField(max_length=None)
    author = models.ForeignKey(User)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class TestCharter(models.Model):
    versions = models.ManyToManyField(Version)
    priority = models.CharField(max_length=15, choices=priority_fields)
    name = models.CharField(max_length=50)
    prerequisites = models.CharField(max_length=50, blank=True, null=True)
    persona = models.ForeignKey(Persona)
    objective = models.TextField(max_length=None)
    scope = models.TextField(max_length=None)
    test_notes = models.TextField(max_length=None)
    author = models.ForeignKey(User)

    def __str__(self):
        return str(self.id) + ' - ' + self.name


class TestGroup(models.Model):
    version = models.ForeignKey(Version)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=None)
    test_cases = models.ManyToManyField(TestCase, blank=True, null=True)
    test_charters = models.ManyToManyField(TestCharter, blank=True, null=True)


class TestResult(models.Model):
    test_case = models.ForeignKey(TestCase)
    test_group = models.ForeignKey(TestGroup)
    result = models.CharField(max_length=15, choices=test_states)
    result_notes = models.TextField(max_length=None)
    tester = models.ForeignKey(User, editable=False)
    execution_date = models.DateTimeField(editable=False)


class TestSession(models.Model):
    test_charter = models.ForeignKey(TestCharter)
    test_group = models.ForeignKey(TestGroup)
    areas_tested = models.TextField(max_length=None, blank=True, null=True)
    notes = models.TextField(max_length=None)
    tester = models.ForeignKey(User, editable=False)
    execution_date = models.DateTimeField(editable=False)


class Defect(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=None)
    status = models.CharField(max_length=15, choices=defect_states)
    priority = models.CharField(max_length=15, choices=priority_fields)
    affected_versions = models.ManyToManyField(
            Version, related_name='affected_versions',
            blank=True, null=True)
    fixed_versions = models.ManyToManyField(
            Version, related_name='fixed_version', blank=True, null=True)
    procedure = models.TextField(max_length=None)
    reporter = models.ForeignKey(User,
                                 related_name='reporter_user')
    assigned = models.ForeignKey(
            User, related_name='assigned_user', blank=True, null=True)
    affected_test_cases = models.ManyToManyField(
            TestCase, blank=True, null=True)
