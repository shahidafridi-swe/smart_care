from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'phone']

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    username.admin_order_field = 'user__username'
    first_name.admin_order_field = 'user__first_name'
    last_name.admin_order_field = 'user__last_name'