from django.shortcuts import render
from .models import StudentWorker, Schedule, DayOffRequest
from datetime import datetime, timedelta

# Create your views here.

def roster_view(request):
    workers = StudentWorker.objects.all()
    return render(request, 'roster/roster.html', {'workers': workers})

def schedule_view(request):
    workers = StudentWorker.objects.all()
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    schedule_matrix = {worker: {day: '' for day in days} for worker in workers}

    for schedule in Schedule.objects.all():
        worker = schedule.student_worker
        day = schedule.day  # 'Mon', 'Tue', etc.
        time = f"{schedule.start_time.strftime('%I:%M %p')} - {schedule.end_time.strftime('%I:%M %p')}"  # AM/PM format
        schedule_matrix[worker][day] = time

    return render(request, 'roster/schedule.html', {'schedule_matrix': schedule_matrix, 'days': days, 'workers': workers})