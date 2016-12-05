from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^check/is_staff$', views.check_is_staff, name='check_is_staff'),
    url(r'^check/is_superuser$', views.check_is_superuser, name='check_is_superuser'),
]

