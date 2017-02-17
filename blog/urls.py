from django.conf.urls import url
from . import view

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
]