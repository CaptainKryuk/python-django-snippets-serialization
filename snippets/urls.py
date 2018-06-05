from django.urls import path
from django.conf.urls import url
from snippets import views


urlpatterns = [
    path('', views.snippet_list, name='snippets_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail, name='snippet_detail')
]