from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from main.models import Version,TestCase, Persona, Defect
from main.forms import VersionForm, TestCaseForm, PersonaForm, DefectForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(home)
    else:
        form = UserCreationForm()
    return render(request, 'main/register_user.html', {'form':form})

@login_required
def home(request):
    return render(request, "main/home.html")


@login_required
def show_test_cases(request, version_id=None):
    context = dict()
    if version_id:
        context['all_test_cases'] = TestCase.objects.filter(versions__id=version_id)
    else:
        context['all_test_cases'] = TestCase.objects.all()
    return render(request, "main/test_cases.html",
    context)

@login_required
def show_test_case(request, test_id):
    context = dict()
    context['test_case'] = TestCase.objects.get(id=test_id)
    return render(request, "main/test_case_details.html",
    context)

@login_required
def new_test_case(request):
    if request.method == 'POST':
        form = TestCaseForm(request.POST)
        if form.is_valid():
            test_case = form.save(commit=False)
            test_case.author = request.user
            test_case.save()
            form.save_m2m()
            return redirect(home)
    else:
        form = TestCaseForm()
    return render(request, 'main/new_test_case.html', {'form':form})

@login_required
def update_test_case(request, id):
    test_case = get_object_or_404(TestCase, pk=id)
    if request.method == 'POST':
        form = TestCaseForm(request.POST or None, instance=test_case)
        if form.is_valid():
            test_case = form.save(commit=False)
            test_case.author = request.user
            test_case.save()
            form.save_m2m()
            return redirect(show_test_cases)
    else:
        form = TestCaseForm(instance = test_case)
    return render(request, 'main/new_test_case.html', {'test_case':test_case,'form':form})

@login_required
def delete_test_case(request, id):
    test_case  = TestCase.objects.get(id=id)
    if test_case:
        test_case.delete()
    return redirect(show_test_cases)

@login_required
def show_versions(request):
    context = dict()
    context['all_versions'] = Version.objects.all()
    return render(request, "main/versions.html",
    context)

@login_required
def new_version(request):
    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            version = form.save(commit=False)
            version.save()
            return redirect(show_versions)
    else:
        form = VersionForm()
    return render(request, 'main/new_version.html', {'form':form})

@login_required
def update_version(request, id):
    version = get_object_or_404(Version, pk=id)
    if request.method == 'POST':
        form = VersionForm(request.POST or None, instance=version)
        if form.is_valid():
            form.save()
            return redirect(show_versions)
    else:
        form = VersionForm(instance = version)
    return render(request, 'main/new_version.html', {'version':version,'form':form})

@login_required
def delete_version(request, id):
    version  = Version.objects.get(id=id)
    if version:
        version.delete()
    return redirect(show_versions)

@login_required
def show_personas(request):
    context = dict()
    context['all_personas'] = Persona.objects.all()
    return render(request, "main/personas.html",
    context)

@login_required
def new_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return redirect(home)
    else:
        form = PersonaForm()
    return render(request, 'main/new_persona.html', {'form':form})

@login_required
def update_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST or None, instance=persona)
        if form.is_valid():
            form.save()
            return redirect(show_personas)
    else:
        form = PersonaForm(instance = persona)
    return render(request, 'main/new_persona.html', {'persona':persona,'form':form})

@login_required
def delete_persona(request, id):
    persona  = Persona.objects.get(id=id)
    if persona:
        persona.delete()
    return redirect(show_personas)

@login_required
def show_defects(request, version_id=None):
    context = dict()
    if version_id:
        context['all_defects'] = Defect.objects.filter(versions__id=version_id)
    else:
        context['all_defects'] = Defect.objects.all()
    return render(request, "main/defects.html",
        context)

@login_required
def show_defect(request, defect_id):
    context = dict()
    context['defect'] = Defect.objects.get(id=defect_id)
    return render(request, "main/defect_details.html",
    context)

@login_required
def new_defect(request):
    if request.method == 'POST':
        form = DefectForm(request.POST)
        if form.is_valid():
            defect = form.save(commit=False)
            defect.reporter = request.user
            defect.save()
            form.save_m2m()
            return redirect(home)
    else:
        form = DefectForm()
    return render(request, 'main/new_defect.html', {'form':form})

@login_required
def update_defect(request, id):
    defect = get_object_or_404(Defect, pk=id)
    if request.method == 'POST':
        form = DefectForm(request.POST or None, instance=defect)
        if form.is_valid():
            defect = form.save(commit=False)
            defect.author = request.user
            defect.save()
            form.save_m2m()
            return redirect(show_defects)
    else:
        form = DefectForm(instance = defect)
    return render(request, 'main/new_defect.html', {'defect':defect,'form':form})

@login_required
def delete_defect(request, id):
    defect  = Defect.objects.get(id=id)
    if defect:
        defect.delete()
    return redirect(show_defects)
