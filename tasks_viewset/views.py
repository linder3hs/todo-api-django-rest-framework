from tasks.models import Todo
from tasks.serializers import TodoSerializer
from .pagination import SimplePagination
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action

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

    @action(detail=True, methods=['get'], url_path="detalle", url_name="detalle")
    def detalle(self, request, pk=None):
        return self.retrieve(request, pk)


class TaskReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']
