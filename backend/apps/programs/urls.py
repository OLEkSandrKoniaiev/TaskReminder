from django.urls import path

from apps.programs.views import ProgramListCreateView, ProgramRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProgramListCreateView.as_view(), name='program-list-create'),
    path('/<int:pk>', ProgramRetrieveUpdateDestroyView.as_view(), name='program-detail-update-delete'),
]
