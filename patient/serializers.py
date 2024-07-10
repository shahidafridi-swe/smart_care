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
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']
        
    
    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error': "Two Password Doesn't Matched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email Already Exists"})
        account = User(username=username, email=email,first_name=first_name,last_name=last_name)
        print(account)
        account.set_password(password)
        account.save()
        return account