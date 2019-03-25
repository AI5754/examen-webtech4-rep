from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^time_remaining/$', views.time_remaining, name='time remaining'),
    # url(r'^.*/$', views.index, name='index'),
]
