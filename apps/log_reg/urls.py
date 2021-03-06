from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^success$', views.success, name='success'),
    url(r'^edit/(?P<id>\d+)$', views.editpage, name='editpage'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^(?P<id>\d+)/update$', views.update_pswd_page),
    url(r'^(?P<id>\d+)/update_pswd$', views.update_pswd),
    url(r'^reset$', views.reset, name='logout'),
]
