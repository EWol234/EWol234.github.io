from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.proj_display, name="proj_display"),
]
