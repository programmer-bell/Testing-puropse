from rest_framework.response import Response
from rest_framework import status
from school.serializers import SchoolSerializer
from rest_framework import generics
from school.models import School


class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'pk'


class SchoolUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    lookup_field = 'pk'
