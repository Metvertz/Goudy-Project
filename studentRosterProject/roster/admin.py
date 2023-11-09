from django.contrib import admin
from .models import StudentWorker, Schedule, DayOffRequest

# Register your models here.

admin.site.register(StudentWorker)
admin.site.register(DayOffRequest)
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('student_worker', 'day', 'start_time', 'end_time')
    list_filter = ('day',)
    ordering = ('day', 'start_time',)