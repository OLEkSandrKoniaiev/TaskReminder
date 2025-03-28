from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import UniversityModel
from .serializers import UniversitySerializer


class UniversityListCreateView(ListCreateAPIView):
    serializer_class = UniversitySerializer
    queryset = UniversityModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UniversityRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UniversitySerializer
    queryset = UniversityModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
