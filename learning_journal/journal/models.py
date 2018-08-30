from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=128)
    created = models.DateField(auto_now_add=True)
    time_spent = models.CharField(max_length=64)
    learned = models.TextField()
    resourses = models.TextField()
