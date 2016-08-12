import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from main.models import Version, TestCase, TestCharter, TestGroup, Persona, Defect, TestResult
from main.forms import VersionForm, TestCaseForm, TestCharterForm, TestGroupForm, PersonaForm, DefectForm, TestResultForm

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
def run_test_case(request, test_group_id, test_case_id):
    if request.method == 'POST':
        form = TestResultForm(request.POST)
        if form.is_valid():
            test_result = form.save(commit=False)
            test_result.test_case = TestCase.objects.get(id=test_case_id)
            test_result.test_group = TestGroup.objects.get(id=test_group_id)
            test_result.tester = request.user
            test_result.execution_date = datetime.datetime.now()
            test_result.save()
            form.save_m2m()
            return show_test_group(request,test_group_id)
    else:
        tr = TestResult.objects.filter(test_case__id=test_case_id, test_group__id=test_group_id).exists()
        if not tr:
            form = TestResultForm()
        else:
            return HttpResponse('Error - Test result has already been recordered for this test case')
    return render(request, 'main/run_test_case.html', {'form':form})

@login_required
def view_test_result(request, result_id=None):
    context = dict()
    if result_id:
        context['result'] = TestResult.objects.get(id=result_id)
    return render(request, "main/test_result.html", context)

@login_required
def show_test_charters(request, version_id=None):
    context = dict()
    if version_id:
        context['all_test_charters'] = TestCharter.objects.filter(versions__id=version_id)
    else:
        context['all_test_charters'] = TestCharter.objects.all()
    return render(request, "main/test_charters.html",
    context)

@login_required
def show_test_charter(request, test_id):
    context = dict()
    context['test_charter'] = TestCharter.objects.get(id=test_id)
    return render(request, "main/test_charter_details.html",
    context)

@login_required
def new_test_charter(request):
    if request.method == 'POST':
        form = TestCharterForm(request.POST)
        if form.is_valid():
            test_charter = form.save(commit=False)
            test_charter.author = request.user
            test_charter.save()
            form.save_m2m()
            return redirect(home)
    else:
        form = TestCharterForm()
    return render(request, 'main/new_test_charter.html', {'form':form})

@login_required
def update_test_charter(request, id):
    test_charter = get_object_or_404(TestCharter, pk=id)
    if request.method == 'POST':
        form = TestCharterForm(request.POST or None, instance=test_charter)
        if form.is_valid():
            test_charter = form.save(commit=False)
            test_charter.author = request.user
            test_charter.save()
            form.save_m2m()
            return redirect(show_test_charters)
    else:
        form = TestCharterForm(instance = test_charter)
    return render(request, 'main/new_test_charter.html', {'test_charter':test_charter,'form':form})

@login_required
def delete_test_charter(request, id):
    test_charter  = TestCharter.objects.get(id=id)
    if test_charter:
        test_charter.delete()
        return redirect(show_test_charters)

@login_required
def show_test_groups(request, version_id=None):
    context = dict()
    if version_id:
        context['all_test_groups'] = TestGroup.objects.filter(version__id=version_id)
        context['version_id'] = version_id
    else:
        context['all_test_groups'] = TestGroup.objects.all()
    return render(request, "main/test_groups.html",
    context)

@login_required
def show_test_group(request, group_id):
    context = dict()
    group = TestGroup.objects.get(id=group_id)
    test_results = []
    result_ids = []
    for test in group.test_cases.all():
        result_set = test.testresult_set.filter(test_group__id=group_id)
        if result_set:
            test_results.append(result_set[0].result)
            result_ids.append(result_set[0].id)
        else:
            test_results.append(None)
            result_ids.append(None)
    context['test_group'] = group
    context['test_cases'] = zip(group.test_cases.all(), test_results, result_ids)
    return render(request, "main/test_group_details.html",
    context)

@login_required
def new_test_group(request, version_id):
    if request.method == 'POST':
        form = TestGroupForm(request.POST)
        if form.is_valid():
            test_group = form.save(commit=False)
            test_group.version =  Version.objects.get(id=version_id)
            test_group.save()
            form.save_m2m()
            return show_test_groups(request, version_id=test_group.version.id)
    else:
        form = TestGroupForm()
    return render(request, 'main/new_test_group.html', {'form':form})

@login_required
def update_test_group(request, id):
    test_group = get_object_or_404(TestGroup, pk=id)
    if request.method == 'POST':
        form = TestGroupForm(request.POST or None, instance=test_group)
        if form.is_valid():
            test_group = form.save(commit=False)
            test_group.save()
            form.save_m2m()
            return show_test_groups(request, version_id=test_group.version.id)
    else:
        form = TestGroupForm(instance = test_group)
    return render(request, 'main/new_test_group.html', {'test_group':test_group,'form':form})

@login_required
def delete_test_group(request, id):
    test_group  = TestGroup.objects.get(id=id)
    if test_group:
        test_group.delete()
        return redirect(show_test_groups)

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
            return show_personas(request)
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
            return show_personas(request)
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
            return show_defects(request)
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
            return show_defects(request)
    else:
        form = DefectForm(instance = defect)
    return render(request, 'main/new_defect.html', {'defect':defect,'form':form})

@login_required
def delete_defect(request, id):
    defect  = Defect.objects.get(id=id)
    if defect:
        defect.delete()
    return redirect(show_defects)
