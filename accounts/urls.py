from django.conf.urls import url, include
from accounts import urls_reset
from .views import index, register, profile, logout, login, edit, change_password


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^(?P<pk>\d+)/edit/$', edit, name='edit_profile'),
    url(r'^(?P<pk>\d+)/password/$', change_password, name='change_password'),
]
