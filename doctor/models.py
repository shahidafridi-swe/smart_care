from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

class Specialization(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="doctor/images/")
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f"Dr.  {self.user.first_name} {self.user.last_name}"
    
STAR_CHOICES = (
    ('★','★'),
    ('★★','★★'),
    ('★★★','★★★'),
    ('★★★★','★★★★'),
    ('★★★★★','★★★★★'),
)

class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.CharField(max_length=10, choices=STAR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Patient: {self.reviewer.user.first_name} - Doctor: {self.doctor.user.first_name}"