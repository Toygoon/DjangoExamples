""" Simple views; Return current date and time """

from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is %s.</body></html>" % now

    return HttpResponse(html)