from django.shortcuts import render
from django.utils import timezone
from .models import TimeEntries
# Create your views here.

def time_app(request):
    #entries = TimeEntries.objects.filter(date_of_work_lte=timezone.now()).order_by('date_of_work')
    entries = TimeEntries.objects.all()
    return render(request, 'time_app/time_app.html', {'entries': entries})


