#urls.py

from django.urls import path

from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^calendar/$', views.CalendarView.as_view(), name='calendar')
]

