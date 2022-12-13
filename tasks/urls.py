"""
from rest_framework.routers import DefaultRouter
from .views import TaskView

router = DefaultRouter()

router.register("todo", TaskView, basename="todo")
"""
from django.urls import path
from .views import TodoView, TodoViewDetail

urlpatterns = [
    path("todo/", TodoView.as_view(), name="todo"),
    path("todo/<id>/", TodoViewDetail.as_view(), name="todo-detail"),
]
