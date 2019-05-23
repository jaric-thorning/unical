from django.shortcuts import render

from django.views.generic import ListView, CreateView, TemplateView
from datetime import datetime, timedelta, date
from django.views import generic

from django.http import HttpResponse
from django.template import loader

from django import forms

from .models import Event 

import calendar
from django.urls import reverse
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe
from .utils import EventCalendar

from .models import Event


import json
# Create your views here.


from django_popup_view_field.registry import registry_popup_view

def searchEvents(request):
	if request.is_ajax():
		q = request.GET.get('term', '')
		events = Event.objects.filter(name__startswith=q)
		results = []
		for event in events:
			results.append(event.name)


		jsonresults = {
			"results" : results
		}

		data = json.dumps(jsonresults)
	
	else:
		data = 'fail'
	
	mimetype = 'application/json'


	print("completed search - returning: {results}")
	
	return HttpResponse(data, mimetype)


class ClubTable(TemplateView):
	
	def get_context_data(self, **kwargs):
		ctx = super(ClubTable, self).get_context_data(**kwargs)
		ctx['clubTableHeader'] = ['Followed Clubs',]
		ctx['clubTableRows'] = [{'name': "UQ Sailing Club",}, {'name': "HMNS",},
			{'name': "UQ Beach Volleyball",}]
		return ctx



class MiniCalendar(TemplateView):
	
	def get_context_data(self,d, **kwargs):
		date = get_date(d) 
		ctx = super(MiniCalendar, self).get_context_data(**kwargs)
		ctx['miniCalendarMonth'] = str(date.strftime('%B'))
		ctx['miniCalendarHeader'] = ['m','t','w','t','f','s','s']
		ctx['miniCalendarRows'] = self.get_calendarRows(date)

		return ctx


	def get_calendarRows(self,d):
		first = d.replace(day=1)
		days_in_month = calendar.monthrange(d.year, d.month)[1]
		index = first.weekday()


		rows = [[]]
		current_row = 0

		#pad start
		for i in range(0, index):
			rows[current_row].append("  ")
		#fill dates
		for i in range(1, days_in_month + 1):
			if(index >= 7):
				index = 0
				current_row += 1
				rows.append([])

			rows[current_row].append(str(i).zfill(2))
			index += 1

		#pad end
		for i in range(index, 7):
			rows[current_row].append("  ")



		rows_json = []

		# print(rows)
		for row in rows:
			rows_json.append({'mon': row[0],'tue': row[1],'wed': row[2],
				'thu': row[3],'fri': row[4],'sat': row[5],'sun': row[6],})

	

		return(rows_json)


class EventView(generic.ListView):
	model = Event
	template_name = 'events/event.html'

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)

		try:
			event = Event.objects.filter(id=self.request.GET.get('event', None))[0]
			context['event'] = event
			context['name'] = event.name

		except:
			context['name'] = "Couldn't find event!"
		
		
		return context






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

		context = {**context, **(ClubTable().get_context_data())}
		context = {**context, **(MiniCalendar().get_context_data(self.request.GET.get('month', None)))}
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