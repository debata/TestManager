"""TestManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from main.forms import LoginForm
from main.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^register/$', register, name='register_user'),
    url(r'^login/$', views.login, {'template_name': 'main/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$',views.logout, {'next_page': views.login}, name='logout'),
    url(r'^version/$', show_versions, name='show_all_versions'),
    url(r'^version/new/$', new_version, name='new_version'),
    url(r'^version/update/([0-9]+)/$', update_version, name='update_version'),
    url(r'^version/delete/([0-9]+)/$', delete_version, name='delete_version'),
    url(r'^persona/$', show_personas, name='show_all_personas'),
    url(r'^persona/new/$', new_persona, name='new_persona'),
    url(r'^persona/update/([0-9]+)/$', update_persona, name='update_persona'),
    url(r'^persona/delete/([0-9]+)/$', delete_persona, name='delete_persona'),
    url(r'^testcase/$', show_test_cases, name='show_all_test_cases'),
    url(r'^testcase/version/$', show_versions),
    url(r'^testcase/version/([0-9]+)/$', show_test_cases, name='show_all_test_cases'),
    url(r'^testcase/new/$', new_test_case, name='new_test_case'),
    url(r'^testcase/([0-9]+)/$', show_test_case, name='test_case_by_id'),
    url(r'^testcase/update/([0-9]+)/$', update_test_case, name='update_test_case'),
    url(r'^testcase/delete/([0-9]+)/$', delete_test_case, name='delete_test_case'),
    url(r'^testcharter/$', show_test_charters, name='show_all_test_charters'),
    url(r'^testcharter/version/$', show_versions),
    url(r'^testcharter/version/([0-9]+)/$', show_test_charters, name='show_all_test_charters'),
    url(r'^testcharter/new/$', new_test_charter, name='new_test_charter'),
    url(r'^testcharter/([0-9]+)/$', show_test_charter, name='test_charter_by_id'),
    url(r'^testcharter/update/([0-9]+)/$', update_test_charter, name='update_test_charter'),
    url(r'^testcharter/delete/([0-9]+)/$', delete_test_charter, name='delete_test_charter'),
    url(r'^testgroup/$', show_test_groups, name='show_all_test_groups'),
    url(r'^testgroup/version/$', show_versions),
    url(r'^testgroup/version/([0-9]+)/$', show_test_groups, name='show_all_test_groups'),
    url(r'^testgroup/new/([0-9]+)/$', new_test_group, name='new_test_group'),
    url(r'^testgroup/([0-9]+)/$', show_test_group, name='test_group_by_id'),
    url(r'^testgroup/update/([0-9]+)/$', update_test_group, name='update_test_group'),
    url(r'^testgroup/delete/([0-9]+)/$', delete_test_group, name='delete_test_group'),
    url(r'^testgroup/([0-9]+)/runtestcase/([0-9]+)/$', run_test_case, name='run_test_case_by_id_from_group'),
    url(r'^testgroup/([0-9]+)/runtestcharter/([0-9]+)/$', run_test_charter, name='run_test_charter_by_id_from_group'),
    url(r'^testresult/([0-9]+)/$', view_test_result, name='view_test_result'),
    url(r'^testsession/([0-9]+)/$', view_test_session, name='view_test_session'),
    url(r'^defect/$', show_defects, name='show_all_defects'),
    url(r'^defect/version/([0-9]+)/$', show_defects, name='show_all_defects'),
    url(r'^defect/new/$', new_defect, name='new_defect'),
    url(r'^defect/([0-9]+)/$', show_defect, name='defect_by_id'),
    url(r'^defect/update/([0-9]+)/$', update_defect, name='update_defect'),
    url(r'^defect/delete/([0-9]+)/$', delete_defect, name='delete_defect')

]
