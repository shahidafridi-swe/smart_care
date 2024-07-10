from django.db import models
from doctor.models import Doctor, AvailableTime
from patient.models import Patient

APPOINTMENT_TYPES = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),
)
APPOINTMENT_STATUS=(
    ('Pending','Pending'),
    ('Running','Running'),
    ('Completed','Completed'),
)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=10, choices=APPOINTMENT_TYPES)
    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default="Pending")
    symptom = models.TextField()
    appointment_time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"Patient: {self.patient.user.first_name} - Doctor: {self.doctor.user.first_name}"
    
