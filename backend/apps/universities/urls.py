from django.urls import path

from .views import UniversityListCreateView, UniversityRetrieveUpdateDestroyView

urlpatterns = [
    path('', UniversityListCreateView.as_view(), name='university-list-create'),
    path('/<int:pk>', UniversityRetrieveUpdateDestroyView.as_view(), name='university-detail-update-delete'),
]
