from django.urls import path
from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.snippet_list, name='snippets_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail, name='snippet_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)