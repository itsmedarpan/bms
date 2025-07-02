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
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    PROVINCE_CHOICES = [
        ('Province 1', 'Province 1'),
        ('Province 2', 'Province 2'),
        ('Bagmati', 'Bagmati'),
        ('Gandaki', 'Gandaki'),
        ('Lumbini', 'Lumbini'),
        ('Karnali', 'Karnali'),
        ('Sudurpashchim', 'Sudurpashchim'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    units = models.PositiveIntegerField(default=1)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    place = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=20, choices=PROVINCE_CHOICES)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Donate(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=10)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
