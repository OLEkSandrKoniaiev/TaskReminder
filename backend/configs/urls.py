from django.urls import include, path

urlpatterns = [
    path('univercities', include('apps.universities.urls')),
]
