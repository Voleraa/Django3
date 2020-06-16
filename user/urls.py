from django.urls import path, re_path
from django.conf.urls import url
from .views import login_view, logout_view, register_view, profile_view, change_profile_view, post_view

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^post/$', post_view, name='post'),
    url(r'^profile/change/$', change_profile_view, name='change_profile'),
]