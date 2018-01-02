from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<chat_id>\d*)$', views.chat_view, name='chat_view'),
    url(r'^groups/(?P<group_id>\d*)$', views.group_view, name='chat_view'),
    url(r'^messages/(?P<message_id>\d*)$', views.message_view, name='message_view'),
]
