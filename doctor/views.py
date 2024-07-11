from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor, Designation, Specialization, AvailableTime,Review
from .serializers import DoctorSerializer, DesignationSerializer, SpecializationSerializer,AvailableTimeSerializer,ReviewSerializer

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
class DesignationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    
class AvailableTimeViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer