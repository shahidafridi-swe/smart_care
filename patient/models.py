from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='patient/images/')
    phone = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)]
    )
    
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} - {self.phone} "