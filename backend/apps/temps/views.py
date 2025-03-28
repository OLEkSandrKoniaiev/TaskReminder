from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly

from .models import TempModel
from .serializers import TempSerializer


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj.user == request.user


class TempListCreateView(ListCreateAPIView):
    serializer_class = TempSerializer
    queryset = TempModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TempRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TempSerializer
    queryset = TempModel.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
