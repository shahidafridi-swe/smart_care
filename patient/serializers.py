from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Patient
        fields = "__all__"
        