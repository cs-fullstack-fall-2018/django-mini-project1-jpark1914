from django.db import models
from django.utils import timezone

# Create your models here.
class TimeEntries(models.Model):
    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    hours = models.IntegerField()
    date_of_work = models.DateTimeField(
        default=timezone.now)
    date_of_entry = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.date_of_work = timezone.now()

    def __str__(self):
        return self.subject

