from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^extras/$', views.extras, name="extras"),
    url(r'^projects/$', views.proj_list, name="proj_list"),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.proj_display, name="proj_display"),
]
