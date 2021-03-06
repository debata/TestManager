from django import forms
from django.forms import Textarea
from django.contrib.auth.forms import AuthenticationForm
from main.models import (Version, TestCase, TestCharter,
                         TestGroup, Persona, Defect,
                         TestResult, TestSession, Comment)
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(
            label="Username", max_length=30,
            widget=forms.TextInput(attrs={'class':
                                   'form-control', 'name': 'username'}))
    password = forms.CharField(
            label="Password", max_length=30,
            widget=forms.PasswordInput(attrs={'class': 'form-control',
                                       'name': 'password'}))


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
        fields = ('versions', 'priority', 'name',
                  'prerequisites', 'persona',  'procedure')


class TestCharterForm(forms.ModelForm):
    class Meta:
        model = TestCharter
        fields = ('versions', 'priority', 'name',
                  'prerequisites', 'persona',  'objective',
                  'scope', 'test_notes')


class TestGroupForm(forms.ModelForm):
    def __init__(self,version,*args,**kwargs):
        super (TestGroupForm,self ).__init__(*args,**kwargs)
        self.fields['test_cases'].queryset = TestCase.objects.filter(versions=version)
        self.fields['test_charters'].queryset = TestCharter.objects.filter(versions=version)
    class Meta:
        model = TestGroup
        fields = ('name', 'description',
                  'test_cases',  'test_charters')


class DefectForm(forms.ModelForm):
    class Meta:
        model = Defect
        fields = ('name', 'description', 'status',
                  'priority', 'affected_versions',
                  'fixed_versions',  'procedure',
                  'assigned', 'affected_test_cases')


class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = ('result', 'result_notes')


class TestSessionForm(forms.ModelForm):
    class Meta:
        model = TestSession
        fields = ('areas_tested', 'notes')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)
        labels = {
            'comment_body': _('Comment'),
        }
        widgets = {
            'comment_body': Textarea(attrs={'cols': 40, 'rows': 6}),
        }
