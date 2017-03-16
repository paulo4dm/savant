from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^matematica$', views.math_list, name='matematica'),
    url(r'^informatica$', views.info_list, name='informatica'),
]