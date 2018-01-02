from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show$', views.index, name='my_view'),
    url(r'^projects/(?P<project_id>\d*)$', views.projects_view, name='projects_view'),
    url(r'^(?P<task_id>\d*)$', views.task_view, name='task_view'),
    url(r'^page$', views.tasks_page, name='tasks_page'),
    url(r'^template$', views.home_view, name='home_view'),
]
