from django.conf.urls import url, include
from django.contrib import admin

from shirtmanager import views

urlpatterns = [
    url(r'^', include('shirtmanager.urls', namespace='shirtmanager')),
    url(r'^admin/', include(admin.site.urls)),
]