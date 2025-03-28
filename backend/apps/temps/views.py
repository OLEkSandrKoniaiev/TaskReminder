from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import TempModel
from .serializers import TempSerializer


class TempListCreateView(ListCreateAPIView):
    serializer_class = TempSerializer
    queryset = TempModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TempRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TempSerializer
    queryset = TempModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Get rid of this in the near future
    def get_object(self):
        obj = super().get_object()

        if self.request.method in ['PUT', 'PATCH', 'DELETE'] and obj.user != self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")

        return obj
