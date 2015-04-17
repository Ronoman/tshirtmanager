from django.conf.urls import url

from shirtmanager import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]