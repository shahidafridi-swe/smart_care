from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('list',views.DoctorViewset)
router.register('designations',views.DesignationViewset)
router.register('specializations',views.SpecializationViewset)
router.register('available_time',views.AvailableTimeViewset)
router.register('reviews',views.ReviewViewset)

urlpatterns = [
    path('', include(router.urls)),
]
