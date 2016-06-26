from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [

    # Handling root URL
    url(r'^$', RedirectView.as_view(pattern_name='landing:index', permanent=False), name='index'),

    url(r'^admin/', admin.site.urls),
    url(r'api/', include('CatracaDigital.api.urls', namespace='api')),
    url(r'core/', include('CatracaDigital.core.urls', namespace='core')),
    url(r'landing/', include('CatracaDigital.landing.urls', namespace='landing'))
]
