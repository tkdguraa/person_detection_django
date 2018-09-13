from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.observation, name='observation'),
    url(r'^add_user/?$', views.add_user, name='add_user'),
    url(r'^remove_record/$',views.remove_record,name='remove_record'),
    url(r'^warning_record/?$', views.warning_record, name='warning_record'),
    url(r'^change_password/?$', views.change_password, name='change_password'),
]