from django.shortcuts import render
from rest_framework import viewsets, pagination
from .models import Doctor, Designation, Specialization, AvailableTime,Review
from .serializers import DoctorSerializer, DesignationSerializer, SpecializationSerializer,AvailableTimeSerializer,ReviewSerializer

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters
    
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    
class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination

    
    
class DesignationViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    
class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    
class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set
    
class AvailableTimeViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]
    
    
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer