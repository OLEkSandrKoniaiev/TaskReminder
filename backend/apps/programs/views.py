from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import ProgramModel
from .serializers import ProgramSerializer


class ProgramListCreateView(ListCreateAPIView):
    serializer_class = ProgramSerializer
    queryset = ProgramModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProgramRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgramSerializer
    queryset = ProgramModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
