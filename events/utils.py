from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
import datetime
from .models import Event


class EventCalendar(HTMLCalendar):
    def __init__(self, events=None):
        super(EventCalendar, self).__init__()
        self.events = events

    def formatday(self, day, weekday, events):
        """
        Return a day as a table cell.
        """
        events_from_day = events.filter(day__day=day)
        events_html = "<ul>"
        for event in events_from_day:

            #if(event.club_image):
                #events_html += event.get_absolute_image_url()
            
            events_html += event.get_absolute_url() + "<br>"


        events_html += "</ul>"

        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)

    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """

        events = Event.objects.filter(day__month=themonth)

        v = []
        a = v.append
        a('<table border="1" cellpadding="0" cellspacing="0" class="calendar">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, events))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)



class EventCalendarWeek(HTMLCalendar):
    def __init__(self, events=None):
        super(EventCalendarWeek, self).__init__()
        self.events = events

    def formatday(self, day, weekday, events):
        """
        Return a day as a table cell.
        """
        events_from_day = events.filter(day__day=day)
        events_html = "<ul>"
        for event in events_from_day:

            #if(event.club_image):
                #events_html += event.get_absolute_image_url()
            
            events_html += event.get_absolute_url() + "<br>"


        events_html += "</ul>"

        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)

    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s


    def getWeek(self, weeks, date):
        for week in weeks: 
            for day in week:
                if day[0] == date:
                    return week


    def formatweekfull(self, theyear, themonth, theday, withyear=True):


        weeks = self.monthdays2calendar(theyear, themonth)
        events = Event.objects.filter(day__month=themonth)

        v = []
        a = v.append
        a('<table border="1" cellpadding="0" cellspacing="0" class="calendar week">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        # for week in self.monthdays2calendar(theyear, themonth):
        #     a(self.formatweek(week, events))
        #     a('\n')
        a(self.formatweek(self.getWeek(weeks, theday), events))
        a('\n')

        a('</table>')
        a('\n')
        return ''.join(v)



    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """

        date = 12

        weeks = self.monthdays2calendar(theyear, themonth)


        events = Event.objects.filter(day__month=themonth)

        v = []
        a = v.append
        a('<table border="1" cellpadding="0" cellspacing="0" class="calendar week">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        # for week in self.monthdays2calendar(theyear, themonth):
        #     a(self.formatweek(week, events))
        #     a('\n')
        a(self.formatweek(self.getWeek(weeks, date), events))
        a('\n')

        a('</table>')
        a('\n')
        return ''.join(v)