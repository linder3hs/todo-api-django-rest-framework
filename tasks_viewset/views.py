from tasks.models import Todo
from tasks.serializers import TodoSerializer
from .pagination import SimplePagination
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

"""
Tenemos 2 atributos que recibe como minimo el ModelViewSet
queryset
serializer_class
"""

class TaskViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = SimplePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'body']
    search_fields = ['title', 'body']


class TaskReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']
