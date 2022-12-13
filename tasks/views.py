from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .serializers import TodoSerializer
from .models import Todo


class TaskView(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


"""
CRUD usando APIView
"""
class TodoView(APIView):
    """APIView ya tiene get, post, put, delete, patch"""
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({
            "ok": True,
            "data": serializer.data
        })

    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "ok": True,
                "message": "TODO created"
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok": False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TodoViewDetail(APIView):
    """Lista por ID"""
    def get(self, request, id):
        todo = get_object_or_404(Todo, pk=id)
        serializer = TodoSerializer(todo)
        return Response({
            "ok": True,
            "data": serializer.data
        })

    """Actualizar por ID"""
    def put(self, request, id):
        todo = get_object_or_404(Todo, pk=id)
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "ok": True,
                "message": "TODO updated"
            })

        return Response({
            "ok": False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    """Eliminar por ID"""
    def delete(self, request, id):
        todo = get_object_or_404(Todo, pk=id)
        todo.delete()
        return Response({
            "ok": True,
            "message": "TODO deleted"
        })
