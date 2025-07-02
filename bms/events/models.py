from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-start_date', '-start_time']
    
class Request(models.Model):
    pass