from django.contrib import admin
from .models import Appointment

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name', 'patient_name', 'appointment_type', 'appointment_status', 'created_at']

    def doctor_name(self, obj):
        return f"{obj.doctor.user.first_name} {obj.doctor.user.last_name}"

    def patient_name(self, obj):
        return f"{obj.patient.user.first_name} {obj.patient.user.last_name}"

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_type == "Online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('online_appointment_email.html', {'user': obj.patient.user, 'doctor': obj.doctor})
            email = EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()            
    