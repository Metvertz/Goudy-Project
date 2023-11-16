from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import StudentWorker, Schedule, DayOffRequest
from django.contrib.auth import login
from .forms import UserRegistrationForm
#from datetime import datetime, timedelta



# Create your views here.
@login_required
def roster_view(request):
    workers = StudentWorker.objects.all()
    return render(request, 'roster/roster.html', {'workers': workers})

@login_required
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

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a login page or home page after registration
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def account_view(request):
    return render(request, 'roster/account.html', {'user': request.user})
