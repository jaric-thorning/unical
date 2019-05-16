from django.shortcuts import render

from django.views.generic import ListView, CreateView, TemplateView
from datetime import datetime, timedelta, date
from django.views import generic

from django.http import HttpResponse
from django.template import loader

from .models import Event 

import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from .utils import EventCalendar

from .models import Event
# Create your views here.



class CalendarView(generic.ListView):
	model = Event
	template_name = 'events/calendar.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		#use today's date for the calendar
		#d = get_date(self.request.GET.get('day', None))


		d = get_date(self.request.GET.get('month', None))
		

		

		#Instantiate our calendar class with today's year and date
		cal = EventCalendar()

		# Call the format month method, which returns our calendar as a table
		html_cal = cal.formatmonth(d.year, d.month, withyear=True)
		#html_cal = html_cal.replace('<td ', '<td  width="150" height="150"')

		
		clubs = ["UQ Sailing Club", "HMNS"]

		context['clubs'] = clubs

		context['calendar'] = mark_safe(html_cal)
		context['prev_month'] = prev_month(d)
		context['next_month'] = next_month(d)

		return context

def get_date(req_day):
	if req_day:
		year, month = (int(x) for x in req_day.split('-'))
		return date(year, month, day=1)
	return datetime.today()

def prev_month(d):
	first = d.replace(day=1)
	prev_month = first - timedelta(days=1)
	month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
	return month

def next_month(d):
	days_in_month = calendar.monthrange(d.year, d.month)[1]
	last = d.replace(day=days_in_month)
	next_month = last + timedelta(days=1)
	month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
	return month