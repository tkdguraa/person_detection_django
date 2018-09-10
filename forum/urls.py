from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/?$', views.post_detail, name='post_detail'),
    url(r'^post/new/?$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/?$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/?$', views.post_remove, name='post_remove'),
    url(r'^signup/?$', views.sign_up, name='signup'),
    url(r'^get_news/?$', views.get_news, name='get_news'),
    url(r'^results/$', views.search, name='search'),
]