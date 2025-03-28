from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly

from apps.tasks.models import TaskModel
from apps.tasks.serializers import TaskSerializer


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj.user == request.user


class TaskListCreateView(ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = TaskModel.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
