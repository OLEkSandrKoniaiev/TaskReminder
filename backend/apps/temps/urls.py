from configs.urls import path

from apps.temps.views import TempListCreateView, TempRetrieveUpdateDestroyView

urlpatterns = [
    path('', TempListCreateView.as_view(), name='temp-list-create'),
    path('/<int:pk>', TempRetrieveUpdateDestroyView.as_view(), name='temp-detail-update-delete'),
]
