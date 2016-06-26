from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^employee/(?P<mobile_id>[a-zA-Z0-9]+)$', views.employee, name='employee-detail'),
    url(r'^register/(?P<mobile_id>[a-zA-Z0-9]+)$', views.register, name='register-detail'),
    url(r'^delete_register/(?P<register_id>\d+)$', views.register_delete, name='register-delete'),
    url(r'^history/(?P<mobile_id>[a-zA-Z0-9]+)$', views.history, name='history'),
]
