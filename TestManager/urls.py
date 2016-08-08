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
    url(r'^$', home),
    url(r'^register/$', register, name='register_user'),
    url(r'^login/$', views.login, {'template_name': 'main/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$',views.logout, {'next_page': views.login}),
    url(r'^versions/$', show_versions, name='show_all_versions'),
    url(r'^version/new/$', new_version, name='new_version'),
    url(r'^version/update/([0-9]+)/$', update_version, name='update_version'),
    url(r'^version/delete/([0-9]+)/$', delete_version, name='delete_version'),
    url(r'^personas/$', show_personas, name='show_all_personas'),
    url(r'^persona/new/$', new_persona, name='new_persona'),
    url(r'^persona/update/([0-9]+)/$', update_persona, name='update_persona'),
    url(r'^persona/delete/([0-9]+)/$', delete_persona, name='delete_persona'),
    url(r'^testcases/$', show_test_cases, name='show_all_test_cases'),
    url(r'^testcases/version/([0-9]+)/$', show_test_cases, name='show_all_test_cases'),
    url(r'^testcase/new/$', new_test_case, name='new_test_case'),
    url(r'^testcase/([0-9]+)/$', show_test_case, name='test_case_by_id'),
    url(r'^testcase/update/([0-9]+)/$', update_test_case, name='update_test_case'),
    url(r'^testcase/delete/([0-9]+)/$', delete_test_case, name='delete_test_case'),
    url(r'^defects/$', show_defects, name='show_all_defects'),
    url(r'^defects/version/([0-9]+)/$', show_defects, name='show_all_defects'),
    url(r'^defect/new/$', new_defect, name='new_defect'),
    url(r'^defect/([0-9]+)/$', show_defect, name='defect_by_id'),
    url(r'^defect/update/([0-9]+)/$', update_defect, name='update_defect'),
    url(r'^defect/delete/([0-9]+)/$', delete_defect, name='delete_defect')

]
