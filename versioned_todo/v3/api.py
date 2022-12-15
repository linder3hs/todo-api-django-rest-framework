from tasks.models import Todo
from rest_framework.viewsets import ModelViewSet
from .serializers import TodoSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.response import Response


class TodoViewSetCustom(ModelViewSet):
    queryset = Todo.objects.all()

    def get_serializer(self, *args, **kwargs):
        return TodoSerializer

    def list(self, request, *args):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args):
        if isinstance(request.data, list):
            serializer = TodoSerializer(data=request.data, many = True)
        else:
            serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        todo = get_object_or_404(self.queryset, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
