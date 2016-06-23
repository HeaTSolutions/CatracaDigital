from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.today, name='today'),
    url(r'^employee/(?P<employee_pk>.+)$', views.employee, name='employee'),
    url(r'^create_employee$', views.create_employee, name='create-employee'),
    url(r'^timetable/(?P<employee_pk>.+)$', views.timetable, name='timetable'),
    url(r'^register/(?P<register_pk>.+)$', views.register, name='register'),
    url(r'^employees$', views.employees, name='employees'),
    url(r'^create_register/(?P<employee_pk>.+)$', views.create_register, name='create-register'),
    url(r'^remove_employee/(?P<employee_pk>.+)$', views.remove_employee, name='remove-employee'),
    url(r'^report/(?P<employee_pk>.+)$', views.report, name='report'),
    url(r'^company$', views.company, name='company'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout', views.logout, name='logout'),
]
