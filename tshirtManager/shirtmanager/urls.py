from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'login/$', views.login_view, name='login'),
    url(r'register/$', views.create_account, name='register')
]