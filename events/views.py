from django.shortcuts import render

from django.views.generic import ListView, CreateView

from .models import Event
# Create your views here.


class HomePageView(ListView):
	model = Event
	template_name = "change_list.html"

