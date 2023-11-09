from django.db import models
import uuid  # for generating unique IDs

# Create your models here.

class StudentWorker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name  # Now the object will be represented by its name

class Schedule(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_worker = models.ForeignKey(StudentWorker, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.get_day_display()} - {self.student_worker.name} ({self.start_time}-{self.end_time})"
    
class DayOffRequest(models.Model):
    student_worker = models.ForeignKey(StudentWorker, on_delete=models.CASCADE)
    day = models.DateField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_worker.name} - {self.day} {'Approved' if self.approved else 'Pending'}"