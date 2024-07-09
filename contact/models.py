from django.db import models
from django.core.validators import MinLengthValidator

class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=11,
        validators=[MinLengthValidator(11)]
    )
    problem = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Us"