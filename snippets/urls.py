from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url('^snippets/$', views.SnippetList.as_view(),
        name='snippets_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),
        name='snippet_detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9])$', views.UserDetail.as_view()),
    url(r'^users/(?P<pk>[0-9])$', views.UserDetail.as_view()),
])
