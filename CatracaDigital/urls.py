from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'core/', include('CatracaDigital.core.urls', namespace='core')),
    url(r'landing/', include('CatracaDigital.landing.urls', namespace='landing'))
]
