from django.urls import path, include
from .views import RegisterView, LoginView, PatientViewSet, DoctorViewSet, PatientDoctorMappingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet)
router.register(r'mappings', PatientDoctorMappingViewSet, basename='mapping')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('mappings/<int:patient_id>/', PatientDoctorMappingViewSet.as_view({'get':'list'}), name='mapping-by-patient'),
    path('', include(router.urls))
]
