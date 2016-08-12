from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from main.models import Version, TestCase, TestCharter, TestGroup, Persona, Defect, TestResult

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('name', 'description')

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('number', 'name', 'description')

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ('versions', 'priority', 'name', 'prerequisites', 'persona',  'procedure')

class TestCharterForm(forms.ModelForm):
    class Meta:
        model = TestCharter
        fields = ('versions', 'priority', 'name', 'prerequisites', 'persona',  'objective', 'scope', 'test_notes')

class TestGroupForm(forms.ModelForm):
    class Meta:
        model = TestGroup
        fields = ( 'name', 'description', 'test_cases',  'test_charters')

class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = ('name', 'description', 'status', 'priority', 'affected_versions', 'fixed_versions',  'procedure', 'assigned', 'affected_test_cases')

class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = ('result', 'result_notes')

