from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import CourseModel
from .serializers import CourseSerializer


class CourseListCreateView(ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CourseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
