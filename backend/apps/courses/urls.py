from django.urls import path

from apps.courses.views import CourseListCreateView, CourseRetrieveUpdateDestroyView

urlpatterns = [
    path('', CourseListCreateView.as_view(), name='course-list-create'),
    path('/<int:pk>', CourseRetrieveUpdateDestroyView.as_view(), name='course-detail-update-delete'),
]
