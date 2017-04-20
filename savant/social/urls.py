from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.profile, name='profile'),
    url(r'^profile/(?P<pk>[0-9]+)/(?P<tab>[1-5]{1})$', views.tabs, name='tabs'),
    url(r'^profile/connection/new/(?P<pk>[0-9]+)/(?P<tutor>[0-9]+)/(?P<area>[0-9]+)$', views.connect, name='connect'),
    url(r'^matematica$', views.math_list, name='matematica'),
    url(r'^informatica$', views.info_list, name='informatica'),
    url(r'^connect-details/(?P<pk>[0-9]+)/(?P<con_user>[0-9]+)/(?P<conexao>[0-9]+)/$', views.connect_details, name='connect-details'),
    url(r'^connect/add/(?P<pk>[0-9]+)/(?P<conexao>[0-9]+)/(?P<tab>[1-5]{1})/$', views.connect_accept, name='connect_accept'),
    url(r'^connect/del/(?P<pk>[0-9]+)/(?P<conexao>[0-9]+)/(?P<tab>[1-5]{1})/$', views.connect_delete, name='connect_delete'),
    url(r'^connect/end/(?P<pk>[0-9]+)/(?P<conexao>[0-9]+)/(?P<tab>[1-5]{1})/$', views.connect_end, name='connect_end'),
]