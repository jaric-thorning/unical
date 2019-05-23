from __future__ import unicode_literals 

from django.db import models
from django.core.exceptions import ValidationError
#from django.core.urlresolvers import reverse
 
from django.urls import reverse

from django.core.files.storage import FileSystemStorage

# Create your models here.

class Club(models.Model):
	
	name = models.CharField(u'Club Name', primary_key=True, max_length=100, help_text = u'Name of Club', blank=True, null=False)
	club_image = models.ImageField(upload_to='images/', max_length=100, blank=False, null=True)

class Event(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(u'Event Name', max_length=100, help_text = u'Name of the Event', blank=True, null=False)
	day = models.DateField(u'Event Date', help_text = u'Day of the event')
	start_time = models.TimeField(u'Start Time', help_text=u'Starting time of event')
	end_time = models.TimeField(u'Finish Time', help_text=u'Finishing time of event')
	club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
	
	club_image = models.ImageField(upload_to='images/', max_length=100, blank=False, null=True)
	description = models.TextField(u'Description', help_text=u'Description', blank=True, null=True)

	class Meta:
		verbose_name = u'Scheduling'
		verbose_name_plural = u'Scheduling'


	def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
		overlap = False
		if new_start == fixed_end or new_end == fixed_start: #edge case
			overlap = False
		elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #inner limits
			overlap = True
		elif new_start <= fixed_start and new_end >= fixed_end: # outer limits
			overlap = True

		return overlap

	def get_absolute_image_url(self):

		url = self.club_image.url
		
		return u'<img src="%s" width="30" height="30" style="padding-right: 5px" alt="ALT">' % (url)

	def get_absolute_url(self):
		# url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])

		url = f"/event/?event={self.id}"
		return u'<a href="%s">%s</a>' % (url, str(self.club.name) + ' - ' + str(self.name))

	def clean(self):
		if self.end_time <= self.start_time:
			raise ValidationError('Ending times must be after starting times')

		events = Event.objects.filter(day=self.day)

		if events.exists():
			for event in events:
				if(event == self):
					continue

				if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
					raise ValidationError('There is an overlap with another event: ' + str(event.day) + \
						', ' + str(event.start_time) + '-' + str(event.end_time))

