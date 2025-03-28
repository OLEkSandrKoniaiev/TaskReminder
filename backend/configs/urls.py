from django.urls import include, path

urlpatterns = [
    path('univercities', include('apps.universities.urls')),
    path('programs', include('apps.programs.urls')),
]
