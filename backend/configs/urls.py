from django.urls import include, path

urlpatterns = [
    path('universities', include('apps.universities.urls')),
    path('programs', include('apps.programs.urls')),
    path('courses', include('apps.courses.urls')),
    path('users', include('apps.users.urls')),
    path('auth', include('apps.auth.urls')),
    path('temps', include('apps.temps.urls')),
    path('tasks', include('apps.tasks.urls')),
]
