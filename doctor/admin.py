from django.contrib import admin
from .models import Doctor, Designation, Specialization, AvailableTime

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name']

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name
    
    
@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(AvailableTime)