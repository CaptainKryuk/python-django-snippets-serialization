from django.urls import path
from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippets_list'),
    url(r'snippets/^(?P<pk>[0-9]+)/$', views.SnippetList.as_view(), name='snippet_detail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9])$', views.UserDetail.as_view()),
    url(r'^api-auth', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)